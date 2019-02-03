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
		if self.moving_left\
			or self.moving_right\
			or self.moving_down\
			or self.moving_up:
			self.fishing_time = False
			self.fishing_direction = -1
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

	def draw_fishing(self, screen, start_pos):
		start_x = start_pos[0]
		start_y = start_pos[1]
		dx = 0
		dy = 0
		if self.fishing_direction == 0:
			start_y += RADIUS/2
			dx = RADIUS*3
		if self.fishing_direction == 1:
			start_x += RADIUS/2
			dy = -1*RADIUS*3
		if self.fishing_direction == 2:
			start_y -= RADIUS/2
			dx = -1*RADIUS*3
		if self.fishing_direction == 3:
			start_x -= RADIUS/2
			dy = RADIUS*3
		
		pygame.draw.line(screen, (0,0,0), \
						 (start_x, start_y), \
						 (start_x + dx, start_y +dy), 5)

	def fish(self):
		pass