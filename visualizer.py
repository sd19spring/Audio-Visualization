"""
Takes input from spotify_data.py and uses it to create a visual
"""
import random
import pygame
from pygame.locals import *

from shape_classes import *
from spotify_data import *

data = {}
data['beats'], data['bars'], data['danceability'], data['loudness'], data['energy'], data['tempo'], data['mood'] = collect_data()

screen = {}
screen['width'] = 832
screen['height'] = 832
screen['fps'] = 30
screen['window'] = pygame.display.set_mode( [screen['width'], screen['height']], pygame.HWSURFACE)
WHITE = (255,255,255)
BLACK = (0, 0, 0)


class Display:
	"""
	The App class is where all the objects are created and the mechanics of the
	game is run.
	"""
	def __init__(self):
		"""
		Creates basic initialization for the variables, clock, etc.
		"""
        self.numshapes = #some form of tempo input
        self.beat_stamps = [] #list of beat timestamps
		#adds the start time of all the beats to the beat_stamps list
		for i in data['beats']:
			self.beat_stamps.append(i['start'])

        self.bar_stamps = [] #list of bar timestamps
		#adds the start time of all the beats to the beat_stamps list
		for i in data['bars']:
			self.bar_stamps.append(i['start'])

        self.colors = [] #some sort of list of colors based on mood info
        self.movement_speeds = [] #list of speeds based on tempo
        #fill shapes with instances of random shapes
        self.shapes = []
		self.clock = pygame.time.Clock()

    def set_style(self):
        """
        Every x seconds or bars change the style (shape, type of movement, etc.)

        Requires refilling self.shapes
        """
        pass

    def update(self):
        """
        updates the positions/sizes of all the shapes
        """
        pass


    def execute(self):
        """
        Actually runs the visualizer to create a display
        """
        pass
