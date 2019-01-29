import pygame
import ship
import spritesheet
import boat

display_width = 800
display_height = 600
dimensions = (display_width, display_height)
display = pygame.display.set_mode(dimensions)

water_blue = (173, 216, 230)

clock = pygame.time.Clock()

done = False

b = boat.Boat(100, 100);

target_x = 300
target_y = 500

while not done:
	display.fill(water_blue)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			target_x = pygame.mouse.get_pos()[0]
			target_y = pygame.mouse.get_pos()[1]

	if b.x < target_x:
		b.x += 1
		if b.y < target_y:
			b.y += 1
			b.set_orientation(7)
		elif b.y > target_y:
			b.y -= 1
			b.set_orientation(1)
		else:
			b.set_orientation(0)
	elif b.x > target_x:
		b.x -= 1
		if b.y < target_y:
			b.y += 1
			b.set_orientation(5)
		elif b.y > target_y:
			b.y -= 1
			b.set_orientation(3)
		else:
			b.set_orientation(4)
	else:
		if b.y < target_y:
			b.y += 1
			b.set_orientation(6)
		elif b.y > target_y:
			b.y -= 1
			b.set_orientation(2)

	b.draw(display)
	pygame.display.update()
	clock.tick(60)

pygame.quit()