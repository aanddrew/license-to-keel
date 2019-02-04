import pygame
import map

WALK_SPEED = 4
RADIUS = 20

class Player:

	def __init__(self):
		self.x = 0
		self.y = 0

		self.speed = WALK_SPEED

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		self.map = None
		self.map_x = 0
		self.map_y = 0

		self.forbidden_blocks = []

		self.fishing_time = False;
		self.fishing_direction = -1
		self.fishing = False

		self.catch_timer = 0

		self.inventory = []

	def set_map(self, mapIn):
		self.map = mapIn

	def draw(self, screen, pos):
		pygame.draw.circle(screen, (255,120,0), pos, RADIUS, RADIUS)

	def current_block(self):
		return self.map.blocks[self.map_x][self.map_y]
	# def next_block(self, ):

	#need to revamp the movement.
	#I have an idea with next_block to simplify this
	def update(self):
		if self.moving_up:
			self.y -= self.speed
		if self.moving_left:
			self.x -= self.speed
		if self.moving_down:
			self.y += self.speed
		if self.moving_right:
			self.x += self.speed

		#the class does not allow movement outside of the map
		#removing this will cause out of bounds errors
		self.map_x = self.x/self.map.pixels_per_block()
		self.map_y = self.y/self.map.pixels_per_block()
		water_edge = False
		#if moving at all
		if self.moving_left\
			or self.moving_right\
			or self.moving_down\
			or self.moving_up:
			self.fishing_time = False
			self.fishing_direction = -1
			# if self.fishing:
			# 	self.fishing = False
		#specific directions
		if self.moving_left:
			if self.map_x <0:
				self.x += self.speed
				self.map_x = 0
			if self.current_block() in self.forbidden_blocks:
				self.x += self.speed
				self.map_x = self.x/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 2

		if self.moving_right:
			if self.map_x > self.map.size-1:
				self.x -= self.speed
				self.map_x = self.map.size-1
			if self.current_block() in self.forbidden_blocks:
				self.x -= self.speed
				self.map_x = self.x/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 0

		if self.moving_down:
			if self.map_y > self.map.size-1:
				self.y -= self.speed
				self.map_y = self.map.size-1
			if self.current_block() in self.forbidden_blocks:
				self.y -= self.speed
				self.map_y = self.y/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 3

		if self.moving_up:
			if self.map_y <0:
				self.y += self.speed
				self.map_y = 0
			if self.current_block() in self.forbidden_blocks:
				self.y += self.speed
				self.map_x = self.y/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 1

		if water_edge:
			self.fishing_time = True

		if not self.fishing_time:
			self.fishing = False

		if self.fishing:
			self.catch_timer += 1

	def key_down(self, event):
		if event.key == pygame.K_w:
			self.moving_up = True
		if event.key == pygame.K_a:
			self.moving_left = True
		if event.key == pygame.K_s:
			self.moving_down = True
		if event.key == pygame.K_d:
			self.moving_right = True

		if event.key == pygame.K_f:
			if not self.fishing:
				self.fishing = True
				self.catch_timer = 0
			else:
				self.fishing = False
				self.catch_timer = 0
	def key_up(self, event):
		if event.key == pygame.K_w:
			self.moving_up = False
		if event.key == pygame.K_a:
			self.moving_left = False
		if event.key == pygame.K_s:
			self.moving_down = False
		if event.key == pygame.K_d:
			self.moving_right = False

	def fish(self):
		pass