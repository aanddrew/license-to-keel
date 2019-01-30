import pygame
# import ship
import spritesheet
import boat
import player
import map

display_width = 800
display_height = 600
dimensions = (display_width, display_height)
display = pygame.display.set_mode(dimensions)
center = (display_width/2, display_height/2)

water_blue = (173, 216, 230)

clock = pygame.time.Clock()

done = False

target_x = 300
target_y = 500

p = player.Player()
m = map.generate_map(40)

# map.load_map('maps/test.map')
# map.generate_blocks(20)

while not done:
	display.fill(water_blue)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			target_x = pygame.mouse.get_pos()[0]
			target_y = pygame.mouse.get_pos()[1]
		

	
	m.draw(display, (0,0))
	p.draw(display, center)

	pygame.display.update()
	clock.tick(60)

pygame.quit()