import random
import pygame, sys
from pygame.locals import
*
from spotify_data import *
from visualizer import *


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
		#probably want to implement a little bit of random in the speeds and sizes
		self.width = 2 * danceability
		self.height = 3 * energy
		#probably want to change color to thresholds
        self.color = [40*valence, 200*valence, 100*valence]
		self.xspeed = danceability/10
		self.yspeed = danceability/10

	def update(self, type = "floaty rectangle"):
		"""
		Every frame it will add the speed to the object to look like motion
		"""
		if type = "floaty rectangle"
			self.x += self.xspeed
			self.y += self.yspeed

			#defines direction of movement and how it leaves screen
			if self.xspeed > 0 and (self.x + self.width) > screen['width']:
				self.x = -self.width
			elif self.xspeed < 0 and self.x < -self.width:
				self.x = screen['width']

			if self.yspeed > 0 and (self.y) > screen['height']:
				self.y = -self.height
			elif self.xspeed < 0 and (self.y + self.height) < -self.width:
				self.x = screen['height']

	def draw(self):
		"""
		Draws the rectangle on the screen
		"""
		pygame.draw.rect(screen['window'], self.color, Rect( [self.x, self.y], [self.width, self.height] ) )


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
