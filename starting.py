import pygame
from pygame.locals import *
import astar
display_width = 1020+2+200
display_height = 810+2-30*5

pygame.init()
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_caption(u'Algorithm Visualization')

white = (255,255,255)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)
grid  = (0,150,255)

black = (0,0,0)

path = []
walls = []
start_node = ()
end_node = ()

		


def button(msg,x,y,w,h,ic,ac,action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	pygame.draw.rect(screen,ac,(x,y,w,h))
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen,ic,(x,y,w,h))
		if click[0] == 1 and action != None:


			action()


	font = pygame.font.SysFont("freesansbold.ttf",25)
	textSurface ,textRect = text_objects(msg,font)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	screen.blit(textSurface, textRect)


def welcome():

	gameExit = False

	while not gameExit:
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				pygame.quit()
	
		message = ['Welcome to this game, Shashank is lonely as fuck','all he know are different pathfinding algorithms,','he will use different algorihms to find his girlfriend']
		counter = 0
		for message in message:
			text = pygame.font.Font('freesansbold.ttf',30)

			TextSurf, TextRect = text_objects(message,text)


			TextRect.center = ((display_width/2),(display_height/2-150+counter))

			counter+=30
			screen.blit(TextSurf, TextRect)

		button("G O !",500,450,100,50,green,green,start_game)

		pygame.display.update()
		screen.fill((0,0,0))


def text_objects(message,font):
	textSurface = font.render(message,False,white)
	return textSurface,textSurface.get_rect()

def draw_walls():
	global walls
	global start_node
	global end_node
	
	button("Start Node='w'",1025,50,190,50,red,(0,0,50),action = None)
	button("end Node='e'",1025,125,190,50,red,(0,0,50),action = None)
	while True:

		for events in pygame.event.get():
			x,y = pygame.mouse.get_pos()
			x = x//30
			y = y//30
			if events.type == pygame.QUIT:
				pygame.quit()
			if pygame.mouse.get_pressed()[0] and x*30<1020 and y*30<400+8*30 :
				
				

				pygame.draw.rect(screen,grid,(x*30,y*30,29,29))
			
				if (x, y) not in walls:
					walls.append((x,y))
				
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_s:
					
					start_node = x,y
					pygame.draw.rect(screen,red,(x*30,y*30,29,29))
					
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_e:
					

					end_node = x,y
					pygame.draw.rect(screen,white,(x*30,y*30,29,29))
		button("A star",1025,200,190,50,red,(0,0,90),action = construct_maze)
		pygame.display.update()
		
	

def start_game():
	gameExit = False
	screen.fill(black)
	draw_grid = False
	global walls
	while not gameExit:

		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				pygame.quit()
				gameExit = True

		if not draw_grid:

			for x in range(0,1020+30,30):
				pygame.draw.line(screen,grid,(0,x),(1020,x),2) #horizontal line

				pygame.draw.line(screen,grid,(x,0),(x,1020), 2)
				clock.tick(60)
				pygame.display.update()
				draw_grid = True

		button("click here to draw wall",1025,50,190,50,red,(0,0,50),action = draw_walls)
		pygame.display.update()


def construct_maze():
	
	global walls
	global start_node
	global end_node
	width = 34
	global path
	height = 22
	maze = [[0 for i in range(height)]for j in range(width)]
	for x in walls:
		maze[x[0]][x[1]] = 1
	draw = []
	path = astar.search(maze,1,start_node, end_node)
	for i,j in enumerate(path):
		for k,l in enumerate(j):
			if l is not -1:
				draw.append((i,k))

	for i in draw:
		print(i)
		pygame.draw.rect(screen,red,(i[0]*30,i[1]*30,29,29))


				
				
		pygame.display.update()

	
# 	draw(path)


# def draw(path):
# 	print(path)
# 	for i in path:
# 		print(i)
# 		pygame.draw.rect(screen,(i[0],i[1],255),(i[0]*30,i[1]*30,29,29))
# 	pygame.display.update()



def main():
	welcome()
	start_game()

main()



