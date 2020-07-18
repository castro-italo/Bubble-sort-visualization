from   sort   import   *


import pygame
import time
import random
from   sys    import   exit
import os



HEIGHT, WIDTH = 800, 600                                # Dimensões da tela
RUNNING       = True                                    # Variável auxiiar que mantem a janela aberta
ICON          = pygame.image.load('assets/sort.png')    # Ícone da jenala

# Criando lista para ser ordenada
lista = list()

for _ in range(25):
	num = random.randint(0, 50)
	lista.append(num)


print(lista)

# Inicializa o pygame
pygame.init()

# Criando a jenale do nosso jogo
screen = pygame.display.set_mode((HEIGHT, WIDTH))

#  Set title and icon
pygame.display.set_caption("Bubble sort visualization")
pygame.display.set_icon(ICON)

# Mantendo a tela aberta
while True:
	# Pegando todos os eventos do nosso jogo
	for event in pygame.event.get():
		# Verifica se o botão de fechar foi clicado, se sim fecha a janela do jogo
		if(event.type == pygame.QUIT):
			pygame.quit()
			exit()
			RUNNING = False

	# Mudando a cor de fundo da tela
	screen.fill((0, 0, 0))

	dist = 0

	# LIMPA TELA | 

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

	# Precisamos atualizar cada frame da tela
	pygame.display.update()
