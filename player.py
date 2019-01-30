import pygame

class Player:

	def __init__(self):
		self.x = 0
		self.y = 0

		self.speed = 4

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def draw(self, screen, pos):
		pygame.draw.circle(screen, (255,120,0), pos, 20, 20)

	def update(self):
		if self.moving_up:
			self.y -= self.speed
		if self.moving_left:
			self.x -= self.speed
		if self.moving_down:
			self.y += self.speed
		if self.moving_right:
			self.x += self.speed

	def key_down(self, event):
		if event.key == pygame.K_w:
			self.moving_up = True
		if event.key == pygame.K_a:
			self.moving_left = True
		if event.key == pygame.K_s:
			self.moving_down = True
		if event.key == pygame.K_d:
			self.moving_right = True
	def key_up(self, event):
		if event.key == pygame.K_w:
			self.moving_up = False
		if event.key == pygame.K_a:
			self.moving_left = False
		if event.key == pygame.K_s:
			self.moving_down = False
		if event.key == pygame.K_d:
			self.moving_right = False