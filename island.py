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
	def __init__(self, size):
		self.maps = []
		for y in range(0, size):
			self.maps.append([])
			for x in range(0, size):
				left_side = (x==0)
				top_side = (y==0)
				right_side = (x==size-1)
				bottom_side = (y==size-1)

				lands = [1, 1, 1,
						 1, 1, 1,
						 1, 1, 1]
				if not left_side and\
				   not right_side and\
				   not top_side and\
				   not bottom_side:
				   lands[4]=0
				if left_side:
					lands[3] = 0
					#set bottom or top corners
					if top_side:
						lands[0] = 0
					if bottom_side:
						lands[6]=0
				if right_side:
					lands[5] = 0
					#set bottom or top corners
					if top_side:
						lands[2] = 0
					if bottom_side:
						lands[8] = 0
				if top_side:
					lands[1] = 0
				if bottom_side:
					lands[7] = 0
				m = map.generate_map(MAP_SIZE, lands)
				self.maps[y].append(m)