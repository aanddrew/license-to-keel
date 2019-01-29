import pygame

class SpriteSheet:

	def __init__(self, folder, num):
		self.sprites = []
		for i in range(0, num):
			path = folder + "/" + str(i) +".png"
			img = pygame.image.load(path)
			self.sprites.append(img)

		self.current_sprite = 0

	def draw(self, screen, loc):
		screen.blit(self.sprites[self.current_sprite], loc)

	def set_sprite(self, num):
		self.current_sprite = num

	def get_height(self):
		return self.sprites[0].get_height()

	def get_width(self):
		return self.sprites[0].get_width()