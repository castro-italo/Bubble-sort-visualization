import time
import pygame


def bubble_sort(array, dist):
	length = len(array)
	for x in range(length-1):
		for y in range(0, length-x-1):
			if(array[y] > array[y+1]):
				print(f"VALOR MENOR -> {array[y]}")
				print(f"VALOR MAIOR -> {array[y+1]}")
				aux = array[y]
				array[y] = array[y+1]
				array[y+1] = aux 
				pygame.draw.rect(screen, (255, 255, 255), [dist, 550, 10, -i])
				time.sleep(1)
	print(array)
