"""
Takes input from spotify_data.py and uses it to create a visual
"""
import random
import time
import pygame
from pygame.locals import *

from shape_classes import *
from spotify_data import *

data = {}
data['beats'], data['bars'], data['danceability'], data['loudness'], data['energy'], data['tempo'], data['mood'], data['duration'] = collect_data()

screen = {}
screen['width'] = 1920
screen['height'] = 1080
screen['fps'] = 90
screen['window'] = pygame.display.set_mode( [screen['width'], screen['height']], pygame.HWSURFACE)
WHITE = (255,255,255)
BLACK = (0, 0, 0)


class Display:
	"""
	The App class is where all the objects are created and the mechanics of the
	visualization is run.
	"""
	def __init__(self):
		"""
		Creates basic initialization for the variables, clock, etc.
		"""
		pygame.init()

		self.numshapes = int(data['tempo']/10) + random.randint(0,5)
		self.beat_stamps = []
		#adds the start time of all the beats to the beat_stamps list
		for i in data['beats']:
			self.beat_stamps.append(i['start'])

		self.bar_stamps = [] #list of bar timestamps
		#adds the start time of all the beats to the beat_stamps list
		for i in data['bars']:
			self.bar_stamps.append(i['start'])

		self.bar_count = 0
		self.beat_count = 0

		#list of colors based on song mood info
		self.colors = []
		self.set_colors()

		self.clock = pygame.time.Clock()
		self.start_time = time.time()
		self.end_time = self.start_time + data['duration']
		self.ellapsed_time = 0
		self.occurred = False
		self.count = 0
		
		#Establish two different types of circles for the visualization: floaty and bubbles
		self.styles = ("floaty", "bubbles")
		self.style = "floaty"
		self.style_count = 0

		self.shapes = []
		self.fill_shapes()

	def set_colors(self):
		"""
		Determines a color palette for the song based on its mood/valence
		"""
		if data['mood'] < 0.25:
		 	self.colors = [(227,252,245), (204,227,250), (234,211,248), (187,187,187)]
		elif data['mood'] >= 0.25 and data['mood'] < 0.5:
		 	self.colors = [(255,155,155), (251,195,176), (236,201,201), (173,216,230)]
		elif data['mood'] >= 0.5 and data['mood'] < 0.75:
		 	self.colors = [(184,77,212), (59,150,253), (67,197,155), (249,143,107)]
		else:
			self.colors = [(236,202,0), (236,155,0), (236,83,0), (249,242,0)]

	def fill_shapes(self):
		"""
		Fills the shapes array with instances of cirlces and rectangles depending
		on the style.
		"""
		if self.style == "floaty":
			for i in range(self.numshapes):
				if bool(random.getrandbits(1)):
					self.shapes.append(Circle(	random.randint(10,screen['width']-10),
												random.randint(10,screen['height']-10),
												data['danceability'],
												data['energy'],
												data['loudness'],
												self.colors[random.randint(0,3)]))
				else:
					self.shapes.append(Rectangle(	random.randint(10,screen['width']-10),
													random.randint(10,screen['height']-10),
													data['danceability'],
													data['energy'],
													data['loudness'],
													self.colors[random.randint(0,3)]))

		if self.style == "bubbles":
			for i in range(self.numshapes):
				self.shapes.append(Circle(	random.randint(10,screen['width']-10),
											random.randint(10,screen['height']-10),
											data['danceability'],
											data['energy'],
											data['loudness'],
											self.colors[random.randint(0,3)]))

	def update(self):
		'''
		Updates the shapes and display style
		'''
		#updates the style and clears the shapes
		if self.bar_count % 16 == 0:
			self.shapes.clear()
			self.style_count += 1
			if self.style_count % 2 == 0:
				self.style = self.styles[0]
				self.fill_shapes()
			else:
				self.style = self.styles[1]
				self.fill_shapes()

		#updates the shapes
		for shape in self.shapes:
			shape.update(self.style)

	def update_beats(self):
		"""
		For the floaty style, it can change direction of the shapes every beat.
		For the bubbles style, every 4 beats the shape might change expand to
		shrink, and every 8 beats the shape will change location
		"""
		#use the count function so that it doesn't update every beat, every n beats
		self.count += 1
		if self.style == "floaty":
			if self.count == 4:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.xspeed *= -1
					if bool(random.getrandbits(1)):
						shape.yspeed *= -1
					self.count = 0

		if self.style == "bubbles":
			if self.count == 4 or self.count == 8:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.expand_speed *= -1
			if self.count == 8:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.move_to_random()
					self.count = 0

		self.beat_count += 1
		if self.beat_count % 4 == 0:
			self.bar_count += 1

	def draw(self):
		"""
		Displays all the objects on the window for each state
		"""
		#draw the screen background
		screen['window'].fill(BLACK)

		#draw the shapes
		for shape in self.shapes:
			shape.draw()

		pygame.display.flip()

	def cleanup(self):
		"""
		Kills the display when it exits the loop and the song ends
		"""
		pygame.quit()
		quit()

	#EXECUTE ALL CODE AND INITIALIZE GAME
	def execute(self):
		"""
		Executes and updates all the code
		"""
		#The while loop ensures the visualization only goes while the song is still playing
		while self.ellapsed_time < self.end_time:
			self.ellapsed_time = time.time() - self.start_time
			#makes sure that the program hasn't reached a new beat
			if self.occurred == True and self.ellapsed_time > (self.beat_stamps[self.beat_count+1] - self.beat_stamps[0]):
				self.occurred = False
			if self.ellapsed_time > self.beat_stamps[self.beat_count] and self.occurred == False:
				self.update_beats()
				self.occurred = True
			self.update()
			self.draw()
			self.clock.tick(screen['fps'])
		self.cleanup()

if __name__ == "__main__":
	disp = Display()
	disp.execute()
