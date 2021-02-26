import pygame
import object as obj

pygame.init()

def createWindow():
    screenSize = (800, 600)
    backgroundColor = (255, 255, 255)

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("The Most Amazing Window Ever Made")
    screen.fill(backgroundColor)

    pygame.Surface.blit(screen, obj.player, (obj.xPos, obj.yPos))

    pygame.display.flip()
