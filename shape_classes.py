import random
import pygame, sys
from pygame.locals import *

from spotify_data import *
from visualizer import *

class Rectangle:
	"""
	Creates a rectangle shape class
	"""
	def __init__(self, x, y, danceability, energy, loudness, color, screen_data):
		"""
		Origin is top right corner
		"""
		#pulls screen data from screen class
		self.screen = screen_data

		#defines x and y position at top right corner
		self.x = x
		self.y = y

		#makes width and height as a function of energy with randomness
		self.width = int(random.randint(100,200)*energy)
		self.height = int(random.randint(100, 200)*energy)

		#gets color from the mood in the visualizer class
		self.color = color
		#defines speeds as a function of danceability
		self.xspeed = danceability*2
		self.yspeed = danceability*2

	def update(self, type):
		"""
		Every frame this method will add the speed to the object's coordinates to make the object move
		"""
		if type == "floaty":
			self.update_floaty()

		elif type == "fly":
			self.update_fly()

	def update_floaty(self):
		"""
		Updates the screen with the floaty style
		"""
		#Changes position constantly
		self.x += self.xspeed
		self.y += self.yspeed

		#Defines how a rectange leaves and re-enters the screen
		if self.xspeed > 0 and (self.x + self.width) > self.screen['width']:
			self.x = -self.width
		elif self.xspeed < 0 and (self.x) < -self.width:
			self.x = self.screen['width']

		if self.yspeed > 0 and (self.y + self.height) > self.screen['height']:
			self.y = -self.height
		elif self.yspeed < 0 and (self.y) < -self.width:
			self.y = self.screen['height']

	def update_fly(self):
		"""
		Updates the screen with the "fly-by" style
		"""
		#Acceleration
		self.xspeed = self.xspeed * 1.0025
		self.yspeed = self.yspeed * 0.999
		#Adds speed with acceleration
		self.x += self.xspeed
		self.y += self.yspeed

		#Defines how a rectange leaves and re-enters the screen
		if self.xspeed > 0 and (self.x + self.width) > self.screen['width']:
			self.x = -self.width


	def move_to_random(self):
		"""
		Moves the rectangle to a random location in the screen
		"""
		self.x = random.randint(10, self.screen['width']- 10)
		self.y = random.randint(10, self.screen['height']- 10)

	def draw(self):
		"""
		Draws the rectangle on the screen
		"""
		pygame.draw.rect(self.screen['window'], self.color, Rect([self.x, self.y], [self.width, self.height]))


class Circle:
    """
	Creates a circle shape class
	"""
    def __init__(self, x, y, danceability, energy, loudness, color, screen_data):
        """
		Initializes the positions, color, and speeds for the circle
		"""
		#pulls screen data from screen class
        self.screen = screen_data

		#position at center
        self.x = x
        self.y = y
		#defines radius based on danceability
        self.radius = int((100*danceability) + random.randint(0,20))
        self.color = color

		#defines speed based on danceability
        self.xspeed = danceability*2
        self.yspeed = danceability*2
        self.expand_speed = loudness/random.randint(20,40)

    def update(self, type):
        """
		Every frame it will add the speed to the object to look like motion
		based on which style type is being implemented
		"""
        if type == "floaty":
            self.update_floaty()

        elif type == "bubbles":
            self.update_bubbles()

        elif type == "fly":
            self.update_fly()

        elif type == "popcorn":
            self.update_popcorn()

    def update_floaty(self):
        """
        Updates the screen with the floaty style
        """
		#constant motion of shape
        self.x += self.xspeed
        self.y += self.yspeed

		#defines how it leaves screen and reappears
        if self.xspeed > 0 and (self.x + self.radius) > self.screen['width']:
            self.x = -self.radius
        elif self.xspeed < 0 and (self.x) < -self.radius:
            self.x = self.screen['width']

        if self.yspeed > 0 and (self.y + self.radius) > self.screen['height']:
            self.y = -self.radius
        elif self.xspeed < 0 and (self.y) < -self.radius:
            self.x = self.screen['height']

    def update_bubbles(self):
        """
        Updates the screen with the bubbles style
        """
		#constant expand/shrink rate
        self.radius += self.expand_speed

		#if the circle is too small reset its location and size
        if self.radius < 5:
            self.move_to_random()
            self.radius = 100
		#if the circle is too big reset it
        if self.radius > 175:
            self.move_to_random()
            self.radius = 100

    def update_fly(self):
        """
		Updates the screen with the "fly-by" style
		"""
		#Acceleration
        self.xspeed = self.xspeed * 1.0025
        self.yspeed = self.yspeed * 0.999
		#Motion with acceleration
        self.x += self.xspeed
        self.y += self.yspeed

		#Defines how a rectange leaves and re-enters the screen
        if self.xspeed > 0 and (self.x + self.radius) > self.screen['width']:
            self.x = -self.radius

    def update_popcorn(self):
        """
		Updates the popcorn style
		"""
		#Move up fast, move sideways not as fast
        self.y += -7*self.yspeed
        self.x += self.xspeed

    def move_to_random(self):
        """
        Moves the circle to a random location in the screen
        """
        self.x = random.randint(10, self.screen['width']- 10)
        self.y = random.randint(10, self.screen['height']- 10)


    def draw(self):
        """
        Draws the circle on the screen
        """
        pygame.draw.circle(self.screen['window'], self.color, [int(self.x), int(self.y)], int(self.radius))
