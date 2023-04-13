import pygame

pygame.init()


width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My game")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    pygame.display.flip()


pygame.quit()