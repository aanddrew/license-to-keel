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

map_size = 50

p = player.Player()
m = map.generate_map(map_size, [1, 1, 1,
								1, 0, 1,
								1, 1, 1])

p.set_map(m)
p.forbidden_blocks = [0]

p.x = map_size*m.pixels_per_block()/2
# p.x = 0
p.y = map_size*m.pixels_per_block()/2

# print(p.current_block())
p.update()
# print(p.current_block())
while p.current_block() ==0:
	p.y -= m.pixels_per_block()
	p.update()

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
		if event.type == pygame.KEYDOWN:
			p.key_down(event)
		if event.type == pygame.KEYUP:
			p.key_up(event)
	p.update()
	
	m.draw(display, (center[0]-p.x,center[1]-p.y))
	p.draw(display, center)

	# print(p.fishing_time)
	if p.fishing_time:
		p.draw_fishing(display, center)

	pygame.display.update()
	clock.tick(60)

pygame.quit()