import pygame

def draw_grid(screen):
    for row in range(10):
        pygame.draw.line(screen, (0,0,0), (row * 50, 0), (row * 50, 500))
        for column in range(10):
            pygame.draw.line(screen, (0,0,0), (0, column * 50), (500, column * 50), 1)

def fill_square(screen, color, pos):
    pygame.draw.rect(screen, color, ((pos[1] * 50) + 1, (pos[0] * 50) + 1, 49, 49))
    pygame.display.update()