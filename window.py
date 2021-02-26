import pygame

def createWindow():
    screenSize = (800, 600)
    backgroundColor = (0, 0, 255)

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("The Most Amazing Window Ever Made")
    screen.fill(backgroundColor)

    pygame.display.flip()
