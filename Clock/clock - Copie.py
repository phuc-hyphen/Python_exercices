import pygame 
import math
import time

# def time_out():
# 	time_out=pygame.display.set_mode((300,300))
# 	run=True
# 	font = pygame.font.SysFont("sans", 45)
# 	text_time = font.render('Time Out', True, BLACK)
# 	while run:
#
#
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:  # bouton X pour sortir
# 				running = False
# 		time_out.blit(text_time,(0,0))
# 		pygame.display.flip()



# start game
pygame.init()
#créer la fenêtre 
screen=pygame.display.set_mode((500,500))#déclarer un variable 

running = True
second=00
minute=00

start=False
reset=False

GREY=(120,120,120) # définir les couleurs
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

font=pygame.font.SysFont("sans",45)
text_plus1=font.render('+',True,BLACK)#créer un variable de text 
text_plus2=font.render('+',True,BLACK)
text_minus1=font.render('-',True,BLACK)
text_minus2=font.render('-',True,BLACK)
text_start = font.render('START',True,BLACK)
text_reset = font.render('RESET',True,BLACK)
text_minute = font.render('Minute',True,BLACK)
text_second = font.render('Second',True,BLACK)

x_second=0
y_second=0
x_minute=0
y_minute=0

while running: # boucle

	screen.fill(GREY)#changer le couleur de la fenêtre

	pygame.draw.rect(screen,WHITE,(100,50,50,50))# créer un rectangle
	pygame.draw.rect(screen,WHITE,(100,160,50,50))# créer un rectangle
	pygame.draw.rect(screen,WHITE,(260,50,50,50))# créer un rectangle
	pygame.draw.rect(screen,WHITE,(260,160,50,50))# créer un rectangle

	pygame.draw.rect(screen,WHITE,(340,50,150,50))# créer un rectangle
	pygame.draw.rect(screen,WHITE,(340,160,150,50))# créer un rectangle

	pygame.draw.circle(screen,BLACK,(250,360),120)# créer un cercle
	pygame.draw.circle(screen,WHITE,(250,360),119)# créer un cercle
	pygame.draw.circle(screen,BLACK,(250,360),1)# créer un cercle

	text_time=font.render(str(minute) + ":" + str(second),True,BLACK) #écrire le temps

	screen.blit(text_plus1,(110,45))# afficher le text 
	screen.blit(text_plus2,(275,45))

	screen.blit(text_minus1,(110,150))
	screen.blit(text_minus2,(275,150))

	screen.blit(text_time,(180,100))
	screen.blit(text_minute,(50,2))
	screen.blit(text_second,(210,2))

	screen.blit(text_start,(350,45))
	screen.blit(text_reset,(350,150))

	mouse_x,mouse_y = pygame.mouse.get_pos()


	for event in pygame.event.get():
		if event.type == pygame.QUIT: # bouton X pour sortir
			running=False
		if event.type==pygame.MOUSEBUTTONDOWN: # détection le clique de la souris
			if event.button==1:
				if mouse_x>100 and mouse_x<150 and mouse_y>50 and mouse_y<100:# bouton plus de minute 
					minute=minute+1
				if mouse_x>100 and mouse_x<150 and mouse_y>160 and mouse_y<210 and minute>0:# bouton moins de minute 
					minute=minute-1
				if mouse_x>260 and mouse_x<310 and mouse_y>50 and mouse_y<100:# bouton plus de second
					second=second+1
					if second>59:
						minute=minute+1
						second=0
				if mouse_x>260 and mouse_x<310 and mouse_y>160 and mouse_y<210 and second>0:# bouton moins de second
					second=second-1
					if minute>0 and second==0:
						minute=minute-1
						second=60
				if mouse_x>340 and mouse_x<490 and mouse_y>50 and mouse_y<100 :# bouton start
						start=True
						reset=False
				if mouse_x>340 and mouse_x<490 and mouse_y>160 and mouse_y<210 :# bouton reset
						reset=True 
						start=False


	if reset==True:
		text_reset = font.render('RESET',True,RED)
		text_start = font.render('START',True,BLACK)

	if start==True:
		text_start = font.render('START',True,RED)
		text_reset = font.render('RESET',True,BLACK)
		if second>0:
			second=second-1
		if second==0 and minute>0:
			minute=minute-1
			second=60
		if second==0 and minute==0:
			text_time = font.render('Time Out', True, RED)
			screen.blit(text_time,(20,240))


		time.sleep(0.1)
		x_second=250+118*math.sin(6*second*math.pi/180)
		y_second=360-118*math.cos(6*second*math.pi/180)
		x_minute=250+59*math.sin(6*minute*math.pi/180)
		y_minute=360-59*math.cos(6*minute*math.pi/180)

		pygame.draw.line(screen,BLACK,(250,360),(x_second,y_second))#créer une longue aguille 
		pygame.draw.line(screen,RED,(250,360),(x_minute,y_minute))#créer une courte aguille 

	pygame.display.flip()

pygame.quit()
