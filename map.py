import pygame
import random

class Map:
	def __init__(self, sizeIn, blocksIn):
		self.size = sizeIn
		
		self.textures=[]
		#texutres[0] is sand
		self.textures.append(pygame.image.load('textures/grass.png'))
		#textures[1] is grass
		self.textures.append(pygame.image.load('textures/sand.png'))

		self.blocks = blocksIn

	def pixels_per_block(self):
		return self.textures[0].get_width()

	def draw(self, screen, pos):
		pixels = self.pixels_per_block()
		for r in range(0, self.size):
			for c in range(0,self.size):
				loc = (pos[0] + (pixels*c), pos[1] + (pixels*r))
				
				if self.blocks[c][r] != 0:
					screen.blit(self.textures[self.blocks[c][r]-1], loc)

def generate_map(size, lands):
	# blocks = []
	# for i in range(0, size):
	# 	blocks.append([])
	# 	for j in range(0, size):
	# 		r = random.randint(0,2)
	# 		blocks[i].append(r)
	blocks = generate_blocks(size, lands)
	m = Map(size, blocks)

	return m

def generate_blocks(size, lands):
	blocks = []
	for i in range(0, size):
		blocks.append([])
		for j in range(0,size):
			blocks[i].append(-1)

	#creating water in the corners
	middle = size/2
	end = size-1

	blocks[0][0] = lands[0]
	blocks[middle][0] = lands[1]
	blocks[end][0] = lands[2]

	blocks[0][middle] = lands[3]
	blocks[middle][middle] = lands[4]
	blocks[end][middle] = lands[5]

	blocks[0][end] = lands[6]
	blocks[middle][end] = lands[7]
	blocks[end][end] = lands[8]

	square = size/2
	if lands[0] == 1:
		for i in range(0, middle/2):
			blocks[0][0+i] = 1
			blocks[0+i][0] = 1
	if lands[2] == 1:
		for i in range(0, middle/2):
			blocks[end][0+i] = 1
			blocks[end-i][0] = 1
	if lands[6] == 1:
		for i in range(0, middle/2):
			blocks[0][end-i] = 1
			blocks[0+i][end] = 1
	if lands[8] == 1:
		for i in range(0, middle/2):
			blocks[end][end-i] = 1
			blocks[end-i][end] = 1

	#sometimes this loop will get stuck forever....
	#don't know how to fix it. 
	done = False
	while not done:
		neg_count = 0
		done = True
		for x in range(0, size):
			for y in range(0,size):
				# print("%x,%y").format(x,y)
				if blocks[x][y] == -1:
					done = False
					neg_count += 1
				elif blocks[x][y] == 0:
					rand = random.randint(0,4)
					try:
						if rand == 0:
							if blocks[x+1][y] == -1:
								blocks[x+1][y] = 0
						elif rand == 1:
							if blocks[x-1][y] == -1:
								blocks[x-1][y] = 0
						elif rand == 2:
							if blocks[x][y+1] == -1:
								blocks[x][y+1] = 0
						elif rand == 3:
							if blocks[x][y-1] == -1:
								blocks[x][y-1] = 0
					except:
						pass
				elif blocks[x][y] == 1:
					rand = random.randint(0,4)
					try:
						if rand == 0:
							if blocks[x+1][y] == -1:
								blocks[x+1][y] = 1
						elif rand == 1:
							if blocks[x-1][y] == -1:
								blocks[x-1][y] = 1
						elif rand == 2:
							if blocks[x][y+1] == -1:
								blocks[x][y+1] = 1
						elif rand == 3:
							if blocks[x][y-1] == -1:
								blocks[x][y-1] = 1
					except:
						pass

		#end while loop right here
	sand_tol = 2
	#these loops make the lands that are within 'tol' blocks
	#	of water turn to sand. kinda like minecraft
	sand_ran = range(-1*sand_tol,sand_tol)
	#Looping over each element of blocks
	for x in range(0, size):
		for y in range(0,size):
			#if the blocks is land
			if blocks[x][y] == 1:
				#compare the blocks around it in the range ran
				for dx in sand_ran:
					for dy in sand_ran:
						#try to check a block, but it might be out of bounds...
						try:
							if blocks[x+dx][y+dy] == 0:
								blocks[x][y] = 2
						except:
							pass
	return blocks



def load_map(filename):
	file = open(filename)
	for line in file:
		print(line)