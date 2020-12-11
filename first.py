import pygame
from random import randint
if __name__ == '__main__':
    size = width, height = 601, 601
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), event.pos, 20)
        pygame.display.flip()
        clock.tick(100)

    pygame.quit()