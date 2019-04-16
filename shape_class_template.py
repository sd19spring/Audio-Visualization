import random

import pygame
from pygame.locals import *
from chicken import *
from PIL import Image

#classes
class Rectangle:
	"""
	Creates a rectangle class for other obstacles to make collision detection
	easy and define the object in the space on the screen.
	"""
	def __init__(self, x, y, w, h):
		"""
		Origin is top right corner
		"""
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def intersects(self, other):
		"""
		Takes two objects and sees if they are in contact
		"""
		left = self.x
		top = self.y
		right = self.x + self.w
		bottom = self.y + self.h

		oleft = other.x
		otop = other.y
		oright = other.x + other.w
		obottom = other.y + other.h

		return not (left >= oright or right <= oleft or top >= obottom or bottom <= otop)


class Chicken(Rectangle):
	"""
	Defines the actor Chicken as a rectangle to use for detection and movement
	on the screen
	"""
	def __init__(self, x, y, w):
		super(Chicken,self).__init__(x,y,w,w)
		#keeps origin so that it can reset
		self.x0, self.x = x, x
		self.y0, self.y = y, y

		#overshowing the chicken rectangle as an image
		img = Image.open('test.png')
		img = img.convert("RGBA")
		datas = img.getdata()

		newData = []
		for item in datas:
			#if background is white, it gets rid of that background
			if(item[0] == 255) and (item[1] == 255) and (item[2] == 255):
				newData.append((255, 255, 255, 0))
			else:
				newData.append(item)

		#saves the new image without a background
		img.putdata(newData)
		img.save("test2.png", "PNG")

		#scales the image to the size of a block
		self.img = pygame.transform.scale(pygame.image.load('test2.png'),(w,w))
		self.imforward = self.img.convert_alpha()


	def reset(self):
		"""
		When game ends/death moves back to start
		"""
		self.x = self.x0
		self.y = self.y0

	def move(self, xdir, ydir):
		"""
		Movement based on the grid so that it moves exactly one "block" at once
		"""
		self.x += xdir * screen['grid']
		self.y += ydir * screen['grid']

	def update(self):
		"""
		keeps chicken on screen
		"""
		if self.x + self.w > screen['width']:
			self.x = screen['width'] - self.w
		if self.x < 0:
			self.x = 0
		if self.y + self.h > screen['width']:
			self.y = screen['width'] - self.w
		if self.y < 0:
			self.y = 0

	def draw(self):
		"""
		Draws the chicken on the screen
		"""
		screen['window'].blit(self.imforward,(self.x,self.y))


class Obstacle(Rectangle):

	def __init__(self, x, y, w, h, s):
		"""
		Creates an obstacle (car, etc.) that is also defined by a rectangle
		"""
		super(Obstacle, self).__init__(x, y, w, h)
		self.speed = s

		#overshowing the chicken rectangle as an image
		if s >= 0:
			img = Image.open('truckright.png')
		else:
			img = Image.open('truckleft.png')
		img = img.convert("RGBA")
		datas = img.getdata()

		newData = []
		for item in datas:
			#if background is white, it gets rid of that background
			if(item[0] == 255) and (item[1] == 255) and (item[2] == 255):
				newData.append((255, 255, 255, 0))
			else:
				newData.append(item)

		#saves the new image without a background
		img.putdata(newData)
		img.save("truck2.png", "PNG")

		#scales the image to the size of a block
		self.truck = pygame.transform.scale(pygame.image.load('truck2.png'),(w,h))
		self.mytruck = self.truck.convert_alpha()

	def update(self):
		"""
		Every frame it will add the speed to the object to look like motion
		"""
		self.x += self.speed
		#defines direction of movement and how it leaves screen
		if self.speed > 0 and self.x > screen['width'] + screen['grid']:
			self.x = -self.w
		elif self.speed < 0 and self.x < -self.w:
			self.x = screen['width']

	def draw(self):
		"""
		Draws the car/truck on the screen
		"""
		screen['window'].blit(self.mytruck,(self.x,self.y))

class Coin(Rectangle):
	"""
	Creates coins that you can collect to increase your score
	"""
	def __init__(self, x, y, w, h):
		"""
		Initializes the positions of the egg randomly but in the lane that is
		given to it. Overlays an image for the rectangle
		"""
		super(Coin, self).__init__(x, y, w, h)
		self.x0, self.x = random.uniform(1,24)*x, random.uniform(1,24)*x
		self.y0, self.y = y, y

		img = Image.open('coin.png')
		img = img.convert("RGBA")
		datas = img.getdata()

		newData = []
		for item in datas:
			#if background is white, it gets rid of that background
			if(item[0] == 255) and (item[1] == 255) and (item[2] == 255):
				newData.append((255, 255, 255, 0))
			else:
				newData.append(item)

		#saves the new image without a background
		img.putdata(newData)
		img.save("coin2.png", "PNG")

		#scales the image to the size of a block
		self.coin = pygame.transform.scale(pygame.image.load('coin2.png'),(int(self.w/1.5),int(self.w/1.5)))
		self.mycoin = self.coin.convert_alpha()

	#when the coin is caught by the chicken it is removed and shows up at the header
	def update(self, score):
		"""
		If you collect one, it displays it next to your score
		"""
		self.x = screen['width']/2 + score.coins*screen['grid']
		self.y = 8

	def reset(self):
		"""
		Moves the coin back to a new random position in the same lane
		"""
		self.x = self.x0
		self.y = self.y0

	def draw(self):
		screen['window'].blit(self.mycoin,(self.x,self.y))

class Lane(Rectangle):
	"""
	Defines a lane on the screen that has cars, etc.
	Adds lanes as a group of pixels by multiplying by the grid
	"""
	def __init__(self, y, t='safety', c=None, n=0, l=0, spc=0, spd=0, coin = False):
		"""
		Defines a lane as a big rectangle going across the screen given a type
		and obstacles in that lane. Also has the option of a color for safe
		spaces and coins/golden eggs to collect
		"""
		super(Lane, self).__init__(0, y * screen['grid'], screen['width'], screen['grid'])
		self.type = t
		self.color = c
		self.obstacles = []
		self.coins = None

		#Randomizes the distance between obstacles
		offset = random.uniform(0, 200)
		for i in range(n):
			self.obstacles.append(Obstacle(offset + spc * i, y * screen['grid'], l * screen['grid'], screen['grid'], spd))
		#creates coin objects in the lane
		if coin:
			self.coins = Coin(screen['grid'], y * screen['grid'], screen['grid'], screen['grid'])

	def check(self, chicken, score):
		"""
		Checks to see if the player hit a car/obstacle and checks to see if
		the player retrieved a golden egg and updates the score
		"""
		checked = False
		for obstacle in self.obstacles:
			if chicken.intersects(obstacle):
				if self.type == 'car':
					chicken.reset()
					checked = True
		if self.coins is not None:
			if chicken.intersects(self.coins):
				self.coins.update(score)
				score.update(30)
		return checked

	def update(self):
		"""
		Updates the obstacle so it moves across the screen
		"""
		for obstacle in self.obstacles:
			obstacle.update()


	def draw(self):
		"""
		Draws all the objects on the screen
		"""
		if self.color is not None:
			pygame.draw.rect( screen['window'], self.color, Rect( [self.x, self.y], [self.w, self.h] ) )
		for obstacle in self.obstacles:
			obstacle.draw()
		if self.coins is not None:
			self.coins.draw()

#SCORE
class Score:
	"""
	Creates a score class to keep track of how many points the player gets
	every game and doesn't reset high score every game
	"""
	def __init__(self):
		self.score = 0
		self.high_score = 0
		self.high_lane = 1
		self.lives = 3
		self.coins = 0

	def update(self, points):
		"""
		Updates the score as the player moves and collects eggs
		"""
		self.score += points
		if self.score > self.high_score:
			self.high_score = self.score

		#Helps for displaying where the egg is once collected
		if points == 30:
			self.coins +=1

	def reset(self):
		"""
		When all lives lost resets the current scores, but not high score
		"""
		self.score = 0
		self.high_lane = 1
		self.lives = 3
