import pygame
import object as obj
import transform as location

pygame.init()

def createWindow():
    screenSize = (800, 600)
    backgroundColor = (255, 255, 255)

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("The Most Amazing Window Ever Made")
    screen.fill(backgroundColor)

    pygame.Surface.blit(screen, obj.player, (location.xPos, location.yPos))

    pygame.display.flip()

def gameLoop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Up")

        pygame.display.flip()
