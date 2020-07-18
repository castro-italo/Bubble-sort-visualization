import pygame
import time
import random
from   sys    import   exit
import os



HEIGHT, WIDTH = 800, 600                                # Screen size
RUNNING       = True                                    # Aux variable that keep widnow open
ICON          = pygame.image.load('assets/sort.png')    # Window size

# Creating a list with random numbers
lista = list()

for _ in range(25):
	num = random.randint(0, 50)
	lista.append(num)


print(lista)

# start pygame
pygame.init()

# Creating a winfow for our game
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Set an icon and title to screen
pygame.display.set_caption("Bubble sort visualization")
pygame.display.set_icon(ICON)

# Keep window open
while True:
	# Taking game events
	for event in pygame.event.get():
		# Quit the game if 'X' was clicked
		if(event.type == pygame.QUIT):
			pygame.quit()
			exit()
			RUNNING = False

	# Chenging background color
	screen.fill((0, 0, 0))

	dist = 0 

	# bubble sort function
	def bubble_sort(array, dist, width):
		length = len(array)
		dist1 = 0
		for x in range(length-1):
			for y in range(0, length-x-1):				
				for i in array:
					dist1 += 30
					pygame.draw.rect(screen, (255, 255, 255), [dist1, 550, 10, -i*10])
				dist1 = 0
				dist += 30
				if(array[y] > array[y+1]):
					print(array)
					aux = array[y]
					array[y] = array[y+1]
					array[y+1] = aux 
					pygame.draw.rect(screen, (255, 0, 0), [dist, 550, 10, -array[y]*10])
					time.sleep(0.1)
					pygame.display.update()
					screen.fill((0, 0, 0))
			dist = 0
			


	bubble_sort(lista, dist, WIDTH)

	for i in range(len(lista)):
		dist += 30
		pygame.draw.rect(screen, (0, 255, 0), [dist, 550, 10, -lista[i]*10])
		time.sleep(0.1)
		pygame.display.update()
	print(lista)
	os.system("pause")

	# Update each frame 
	pygame.display.update()
