import pygame
import window as wnd

wnd.createWindow()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
