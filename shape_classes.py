import random

import pygame, sys
from pygame.locals import *


class Rectangle:
	"""
	Creates a rectangle class
	"""
	def __init__(self, x, y, danceability, energy, valence):
		"""
		Origin is top right corner
		"""
		self.x = x
		self.y = y
		self.width = 2 * danceability
		self.height = 3 * energy
        self.color = [40*valence, 200*valence, 100*valence]

    def draw(self):
		"""
		Draws the rectangle on the screen
		"""
		pygame.draw.rect(screen['window'], self.color, Rect( [self.x, self.y], [self.w, self.h] ) )

	def move(self, xdir, ydir):
		"""
		Movement based on the grid so that it moves exactly one "block" at once
		"""
		self.x += xdir * screen['grid']
		self.y += ydir * screen['grid']

class Circle:
    """
	Creates a circle class
	"""
    def __init__(self, center, danceability, energy, valence):
        self.center = center
        self.radius = danceability * energy
        self.color = [40*valence, 200*valence, 100*valence]

    def draw(self):
    	"""
    	Draws the circle on the screen
    	"""
    	pygame.draw.circle(screen['window'], self.color, self.center, self.radius)
