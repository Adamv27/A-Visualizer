import draw
import math
import pygame
from aStar import *

pygame.init()
pygame.display.set_caption('A* Visualizer')

screen = pygame.display.set_mode((500, 500))

# COLORS
START_NODE = (193, 99, 255)
END_NODE = (255, 0, 0)
WALL = (122, 122, 122)
BEST_NODE = (255,214,48)

class Visualize:
    def __init__(self):
        self.grid = self.create_grid()
        self.areas = self.get_areas()
        self.start = (4, 0)
        self.end = (4, 9)

    def create_grid(self):
        grid = []
        for row in range(10):
            row = []
            for column in range(10):
                row.append(0)
            grid.append(row)
        return grid

    def get_areas(self):
        areas = []
        for row in range(10):
            for column in range(10):
                areas.append(pygame.Rect(pygame.Rect((row * 50), (column * 50), 50, 50)))
        return areas

    def get_best_path(self, screen):
        best_path = astar(screen, self.grid, self.start, self.end)
        for square in best_path:
            draw.fill_square(screen, BEST_NODE, square)
        return best_path
    def print_grid(self):
        for row in self.grid:
            print(row)


def get_node(visualize, wall):
    if not wall:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for area in visualize.areas:
                            if area.collidepoint(event.pos):
                                row = visualize.areas.index(area) % 10
                                column = math.floor(visualize.areas.index(area) / 10)
                                return row, column
    if wall:
        pos = pygame.mouse.get_pos()
        row = math.floor(pos[1] / 50)
        column = math.floor(pos[0] / 50)
        return row, column


def get_wall(visualize):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousedown = True
                while mousedown:
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEBUTTONUP:
                            print('up')
                            mousedown = False

                        wall_pos = get_node(visualize, True)
                        visualize.grid[wall_pos[0]][wall_pos[1]] = 1
                        draw.fill_square(screen, WALL, wall_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


visualize = Visualize()
screen.fill((255, 255, 255))
draw.draw_grid(screen)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    visualize.start = get_node(visualize, False)
    draw.fill_square(screen, START_NODE, visualize.start)

    visualize.end = get_node(visualize, False)
    draw.fill_square(screen, END_NODE, visualize.end)
    get_wall(visualize)

    print(visualize.get_best_path(screen))
