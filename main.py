import pygame
import window as wnd

pygame.init()

wnd.createWindow()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
