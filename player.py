import pygame

class Player:

	def __init__(self):
		self.x = 0
		self.y = 0

	def draw(self, screen, pos):
		pygame.draw.circle(screen, (0,120,0), pos, 20, 20)