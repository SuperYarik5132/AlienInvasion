# Задача 4
# Яромира горелкова
# 20.01.2024

import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
    display.fill((0, 0, 0))
    pygame.display.flip()