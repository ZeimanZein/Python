import pygame

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My game")

font = pygame.font.Font(None, 36)

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                score += 1
            elif event.key == pygame.K_DOWN:
                score -= 1

    screen.fill((255, 255, 255))

    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()