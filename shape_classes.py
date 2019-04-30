import random
import pygame, sys
from pygame.locals import *

from spotify_data import *
from visualizer import *


class Rectangle:
	"""
	Creates a rectangle shape class
	"""
	def __init__(self, x, y, danceability, energy, loudness, color):
		"""
		Origin is top right corner
		"""
		self.x = x
		self.y = y
		#probably want to implement a little bit of random in the speeds and sizes
		self.width = int(random.randint(100,200)*energy)
		self.height = int(random.randint(100, 200)*energy)

		self.color = color
		self.xspeed = danceability*2
		self.yspeed = danceability*2
		self.expand_speed = loudness/random.randint(20,40)

	def update(self, type = "floaty"):
		"""
		Every frame this method will add the speed to the object's coordinates to make the object move
		"""
		if type == "floaty":
			self.x += self.xspeed
			self.y += self.yspeed

			#Defines how a rectange leaves and re-enters the screen
			if self.xspeed > 0 and (self.x + self.width) > screen['width']:
				self.x = -self.width
			elif self.xspeed < 0 and (self.x) < -self.width:
				self.x = screen['width']

			if self.yspeed > 0 and (self.y + self.height) > screen['height']:
				self.y = -self.height
			elif self.xspeed < 0 and (self.y) < -self.width:
				self.x = screen['height']

	def move_to_random(self):
		"""
		Moves the rectangle to a random location in the screen
		"""
		self.x = random.randint(10, screen['width']- 10)
		self.y = random.randint(10, screen['height']- 10)

	def draw(self):
		"""
		Draws the rectangle on the screen
		"""
		pygame.draw.rect(screen['window'], self.color, Rect([self.x, self.y], [self.width, self.height]))


class Circle:
    """
	Creates a circle shape class
	"""
    def __init__(self, x, y, danceability, energy, loudness, color):
        """
		Initializes the positions, color, and speeds for the circle
		"""
        self.x = x
        self.y = y
        self.radius = int((100*danceability) + random.randint(0,20))
        self.color = color

        self.xspeed = danceability*2
        self.yspeed = danceability*2
        self.expand_speed = loudness/random.randint(20,40)

    def update(self, type = "floaty"):
        """
		Every frame it will add the speed to the object to look like motion
		"""
        if type == "floaty":
            self.x += self.xspeed
            self.y += self.yspeed

			#defines how it leaves screen and reappears
            if self.xspeed > 0 and (self.x + self.radius) > screen['width']:
                self.x = -self.radius
            elif self.xspeed < 0 and (self.x) < -self.radius:
                self.x = screen['width']

            if self.yspeed > 0 and (self.y + self.radius) > screen['height']:
                self.y = -self.radius
            elif self.xspeed < 0 and (self.y) < -self.radius:
                self.x = screen['height']

        elif type == "bubbles":
            self.radius += self.expand_speed

			#if the circle is too small reset its location and size
            if self.radius < 5:
                self.move_to_random()
                self.radius = 50
			#if the circle is too big reset it
            if self.radius > 200:
                self.move_to_random()
                self.radius = 100

    def move_to_random(self):
        """
        Moves the circle to a random location in the screen
        """
        self.x = random.randint(10, screen['width']- 10)
        self.y = random.randint(10, screen['height']- 10)


    def draw(self):
        """
        Draws the circle on the screen
        """
        pygame.draw.circle(screen['window'], self.color, [int(self.x), int(self.y)], int(self.radius))

"""
class Style(numshapes):
	"""
	Creates a generic style class with shapes that can be applied to all other
	styles.
	"""

class Floaty(Style):
	"""
	Creates a Floaty style that adds additional object parameters for this
	specific style and contains an update function specific to the floaty style
	"""

class Bubbles(Style):
	"""
	Creates a Bubbles style that adds additional object parameters for this
	specific style and contains an update function specific to the bubbles style
	"""
"""
