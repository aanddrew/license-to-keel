import pygame
import map

MAP_SIZE = 50

class Island(self, size):
	maps = []
	for y in range(0, size):
		map.append([])
		for x in range(0, size):
			left_side = False
			top_side = False
			right_side = False
			bottom_side = False

			lands = [1, 1, 1,
					 1, 0, 1,
					 1, 1, 1]
			map m = map.generate_map(MAP_SIZE)
			map[y].append(m)