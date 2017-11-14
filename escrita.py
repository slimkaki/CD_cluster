import pygame,sys,time

pygame.init()

screen=pygame.display.set_mode((1200,720),0,32)
pygame.display.set_caption('Cluster K-means')
#myfont=pygame.font.Font("Helvetica.ttf", 40)
mouse = pygame.mouse
canvas = screen.copy()

#                     R    G    B
BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)



canvas.fill(WHITE)

while(True):
	left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key==K_ESCAPE:
				pygame.quit()
		elif left_pressed:
			pygame.draw.circle(canvas, BLACK, (pygame.mouse.get_pos()),5)

	screen.fill(WHITE)
	screen.blit(canvas, (0, 0))
	pygame.mouse.get_pos()
	pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 5)
	pygame.display.update()