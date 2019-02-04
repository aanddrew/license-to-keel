import pygame
import player
import random

pygame.font.init()

game_font = pygame.font.SysFont(pygame.font.get_default_font(), 45)
text_surface = game_font.render('test', False, (0,0,0))

def draw_catch():
	pass

def press_f_to_fish(screen, center):
	text_surface = game_font.render('Press F to Fish', False, (0,0,0))

	draw_x = center[0]-text_surface.get_width()/2
	draw_y = center[1]+100

	back_rect = pygame.rect.Rect(draw_x-5, draw_y-5, \
								 text_surface.get_width()+10,\
								 text_surface.get_height()+10)

	screen.fill((255,127,0), back_rect)
	screen.blit(text_surface, (draw_x, draw_y))
	pass

def draw_fishing(p, screen, start_pos):
	start_x = start_pos[0]
	start_y = start_pos[1]
	dx = 0
	dy = 0

	rand = random.randint(-1*p.catch_timer, p.catch_timer)

	if p.fishing_direction == 0:
		start_y += player.RADIUS/2
		dx = player.RADIUS*3
		dy = rand
	if p.fishing_direction == 1:
		start_x += player.RADIUS/2
		dy = -1*player.RADIUS*3
		dx = rand
	if p.fishing_direction == 2:
		start_y -= player.RADIUS/2
		dx = -1*player.RADIUS*3
		dy = rand
	if p.fishing_direction == 3:
		start_x -= player.RADIUS/2
		dy = player.RADIUS*3
		dx = rand

	pygame.draw.line(screen, (0,0,0), \
					 (start_x, start_y), \
					 (start_x + dx, start_y +dy), 5)