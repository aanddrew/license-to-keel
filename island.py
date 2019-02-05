import pygame
import map

MAP_SIZE = 50

"""
An island is a collection of maps. Most of the islands I think
Will be donut shaped. This is simple to make with how I have them set up

The player will be able to take a ferry or something between islands.
And each new island the player visits will be a higher "level" than
the last one. This will in a sense create an infinite game.
"""
class Island:
	def __init__(self, size, levelIn):
		self.maps = []
		self.level = levelIn
		for x in range(0, size):
			self.maps.append([])
			for y in range(0, size):
				left_side = (x==0)
				top_side = (y==0)
				right_side = (x==size-1)
				bottom_side = (y==size-1)

				lands = [1, 1, 1,
						 1, 1, 1,
						 1, 1, 1]
				#CORNERS
				if x == 0 and y == 0:
					lands = [0, 0, 0,
							 0, 1, 1,
							 0, 1, 1]
				elif x == 0 and y == size-1:
					lands = [0, 0, 0,
							 1, 1, 0,
							 1, 1, 0]
				elif x == size-1 and y == 0:
					lands = [0, 1, 1,
							 0, 1, 1,
							 0, 0, 0]
				elif x == size-1 and y == size-1:
					lands = [1, 1, 0,
							 1, 1, 0,
							 0, 0, 0]
				#SIDES
				elif x == 0:
					lands = [0, 0, 1,
							 0, 0, 1,
							 0, 0, 1]
				elif x == size-1:
					lands = [1, 0, 0,
							 1, 0, 0,
							 1, 0, 0]
				elif y == 0:
					lands = [0, 0, 0,
							 0, 0, 0,
							 1, 1, 1]
				elif y == size-1:
					lands = [1, 1, 1,
							 0, 0, 0,
							 0, 0, 0]
				#MIDDLE
				elif y == size/2 and x == size/2:
					lands = [1, 1, 1,
							 1, 0, 1,
							 1, 1, 1]
				m = map.generate_map(MAP_SIZE, lands, levelIn)
				self.maps[x].append(m)