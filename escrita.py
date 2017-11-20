import pygame,sys,time

pygame.init()

screen=pygame.display.set_mode((280,280),0,32)
pygame.display.set_caption('Cluster K-means')
myfont=pygame.font.Font("VeraMoBd.ttf", 25)
mouse = pygame.mouse
canvas = screen.copy()

#                     R    G    B
BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)

apaga=myfont.render("Apagar",1,(255,255,255))
envia=myfont.render("Enviar",1,(255,255,255))

rect=pygame.Rect(25,25,100,50)



canvas.fill(WHITE)

while(True):
	left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key==K_ESCAPE:
				pygame.quit()
			if event.key==K_RETURN:
				pygame.image.save(screen)
		elif left_pressed:
			pygame.draw.circle(canvas, BLACK, (pygame.mouse.get_pos()),5)

	screen.fill(WHITE)
	screen.blit(canvas, (0, 0))
	pygame.mouse.get_pos()
	pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 5)

	#pygame.draw.rect(screen, (0,0,0),(50,50,120,60))
	#screen.blit(apaga, (62,60))
	#pygame.draw.rect(screen, (0,0,0),(950,50,1000,60))
	#screen.blit(envia, (950,50))
	pygame.display.update()