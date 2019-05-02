"""
Takes input from spotify_data.py and uses it to create a visual
"""
import random
import time
import pygame
from pygame.locals import *

from shape_classes import *
from spotify_data import *

#pauses the song
pause_song()

#collects data about the current song
data = {}
data['beats'], data['bars'], data['danceability'], data['loudness'], data['energy'], data['tempo'], data['mood'], data['duration'] = collect_data()

#sets up the PyGame screen
screen = {}
screen['width'] = 1920
screen['height'] = 1080
screen['fps'] = 120
screen['window'] = pygame.display.set_mode( [screen['width'], screen['height']], pygame.HWSURFACE)
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

		self.numshapes = int(data['tempo']/7) + random.randint(2,5)
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
		self.end_time = data['duration']
		self.ellapsed_time = 0
		self.occurred = False
		self.count = 1

		#Establish two different types of circles for the visualization: floaty and bubbles
		self.styles = ("floaty", "bubbles", "fly", "popcorn")
		self.style = "floaty"
		self.style_count = 1

		self.shapes = []
		self.fill_shapes()

	def set_colors(self):
		"""
		Determines a color palette for the song based on its mood/valence
		"""
		if data['mood'] < 0.25:
		 	self.colors = [(1,31,75), (3,57,108), (0,91,150), (100,151,177), (179,205,224)]
		elif data['mood'] >= 0.25 and data['mood'] < 0.5:
		 	self.colors = [(206,0,0), (133,46,182), (165,26,26), (51,33,169), (9,6,94)]
		elif data['mood'] >= 0.5 and data['mood'] < 0.75:
		 	self.colors = [(255,158,158), (115,246,144), (93,216,126), (49,171,113), (255,98,98)]
		else:
			self.colors = [(236,202,0), (236,155,0), (236,83,0), (249,242,0), (113,199,236)]

	def fill_shapes(self):
		"""
		Fills the shapes array with instances of cirlces and rectangles depending
		on the style.
		"""
		if self.style == "floaty" or self.style == "fly":
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

		elif self.style == "bubbles":
			for i in range(self.numshapes):
				self.shapes.append(Circle(	random.randint(10,screen['width']-10),
											random.randint(10,screen['height']-10),
											data['danceability'],
											data['energy'],
											data['loudness'],
											self.colors[random.randint(0,3)]))

		else:
			for i in range(int(self.numshapes/2)):
				self.shapes.append(Circle(	random.randint(10,screen['width']-10),
											random.randint(10,screen['height']-10),
											data['danceability'],
											data['energy'],
											data['loudness'],
											self.colors[random.randint(0,3)]))

	def update(self):
		'''
		Updates the shapes and display style. Also creates a transition between
		styles during every 8th bar
		'''
		#updates the style and clears the shapes

		if self.bar_count % 8 == 0:
			self.count = 1
			self.shapes.clear()
			self.style_count += 1
			if self.style_count == 2:
				self.style = self.styles[0]
				self.fill_shapes()
			elif self.style_count == 3:
				self.style = self.styles[1]
				self.fill_shapes()
			elif self.style_count == 4:
				self.style = self.styles[2]
				self.fill_shapes()
			else:
				self.style = self.styles[3]
				self.fill_shapes()
			if self.style_count == 5:
				self.style_count = 1

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
			if self.count % 2 == 0:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.xspeed = -shape.xspeed
					if bool(random.getrandbits(1)):
						shape.yspeed = -shape.yspeed

		if self.style == "bubbles":
			if self.count % 4 == 0:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.expand_speed = -shape.expand_speed
			if self.count % 8 == 0:
				for shape in self.shapes:
					if bool(random.getrandbits(1)):
						shape.move_to_random()

		if self.style == "fly":
			for shape in self.shapes:
				shape.yspeed = -shape.yspeed

		if self.style == "popcorn":
			if len(self.shapes) < self.numshapes:
				self.shapes.append(Circle(	random.randint(10,screen['width']-10),
											random.randint(10,screen['height']-10),
											data['danceability'],
											data['energy'],
											data['loudness'],
											self.colors[random.randint(0,3)]))
			for shape in self.shapes:
				if bool(random.getrandbits(1)):
					shape.xspeed = -shape.xspeed
				shape.move_to_random()

		self.beat_count += 1
		if self.beat_count % 4 == 0:
			self.bar_count += 1

	def draw(self):
		"""
		Displays all the objects on the window for each state
		"""
		#draw the screen background
		screen['window'].fill(self.colors[-1])

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
		#unpauses the song right before the first update
		self.start_time = time.time()
		unpause_song()
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
