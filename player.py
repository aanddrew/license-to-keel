import pygame
import map
import random

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
		self.wait_frames = 0
		self.catch_tolerance = 60

		self.at_edge = False;
		self.edge_direction = -1

		self.transporting = False
		self.next_map=(0,0)

		self.inventory = []

	def set_map(self, mapIn):
		self.map = mapIn

	def draw(self, screen, pos):
		pygame.draw.circle(screen, (255,120,0), pos, RADIUS, RADIUS)

	def current_block(self):
		try:
			return self.map.blocks[self.map_x][self.map_y]
		except:
			pass
	# def next_block(self, ):

	def change_wait_frames(self, new = -1):
		if new == -1:
			self.wait_frames = 240 + random.randint(0,120)
		else:
			self.wait_frames = new

	def update_loc(self):
		self.map_x = self.x/self.map.pixels_per_block()
		self.map_y = self.y/self.map.pixels_per_block()

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
		self.update_loc()
		water_edge = False
		#if moving at all
		if self.moving_left\
			or self.moving_right\
			or self.moving_down\
			or self.moving_up:
			self.fishing_time = False
			self.fishing_direction = -1
			self.at_edge = False
			self.edge_direction = -1
			# if self.fishing:
			# 	self.fishing = False
		#specific directions
		if self.moving_left:
			if self.map_x <0:
				self.x += self.speed
				self.map_x = 0
				self.at_edge = True
				self.edge_direction = 2

			if self.current_block() in self.forbidden_blocks:
				self.x += self.speed
				self.map_x = self.x/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 2

		if self.moving_right:
			if self.map_x > self.map.size-1:
				self.x -= self.speed
				self.map_x = self.map.size-1

				self.at_edge = True
				self.edge_direction = 0

			if self.current_block() in self.forbidden_blocks:
				self.x -= self.speed
				self.map_x = self.x/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 0

		if self.moving_down:
			if self.map_y > self.map.size-1:
				self.y -= self.speed
				self.map_y = self.map.size-1

				self.at_edge = True
				self.edge_direction = 3

			if self.current_block() in self.forbidden_blocks:
				self.y -= self.speed
				self.map_y = self.y/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 3

		if self.moving_up:
			if self.map_y <0:
				self.y += self.speed
				self.map_y = 0

				self.at_edge = True
				self.edge_direction = 1

			if self.current_block() in self.forbidden_blocks:
				self.y += self.speed
				self.map_x = self.y/self.map.pixels_per_block()

				water_edge = True
				self.fishing_direction = 1

		#if the player is by the edge of a water, they can fish
		if water_edge:
			self.fishing_time = True

		#if the player walks away from the fishing spot
		if not self.fishing_time:
			self.fishing = False

		if self.fishing:
			self.catch_timer += 1
			if self.catch_timer == (self.wait_frames + self.catch_tolerance):
				self.catch_timer = 0
				self.change_wait_frames()
		# print(self.catch_timer, self.wait_frames)

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
				self.change_wait_frames()
			#if the player is fishing. game time!
			else:
				#if the player has caught the fish
				if self.catch_timer > self.wait_frames:
					print("You caught the fish!")
				else:
					print("You suck lol")
				self.fishing = False
				self.catch_timer = 0
		if event.key == pygame.K_SPACE:
			if self.at_edge:
				self.transporting = True
				if self.edge_direction == 0:
					self.next_map = (1,0)
				elif self.edge_direction == 1:
					self.next_map = (0,-1)
				elif self.edge_direction == 2:
					self.next_map = (-1,0)
				elif self.edge_direction == 3:
					self.next_map = (0,1)
				# print("transporting", self.edge_direction)
		
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