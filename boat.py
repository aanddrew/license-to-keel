import pygame
import spritesheet

class Boat:

	def __init__(self, xIn, yIn):
		#these are the x and y of the center of the boat
		self.x = xIn
		self.y = yIn

		self.ss = spritesheet.SpriteSheet('boat', 8)

	def draw(self, screen):
		#draw the boat so that the x and y are the center of the image
		self.ss.draw(screen, (self.x - self.ss.get_width()/2, 
							  self.y - self.ss.get_height()/2))

	def set_orientation(self, num):
		self.ss.set_sprite(num)