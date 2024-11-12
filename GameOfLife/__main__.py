
import pygame
import numpy as np


ROWS, COLS = 10, 10
CELL_SIZE = 50
GRID_WIDTH, GRID_HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
WHITE, BLACK, BLUE = (255, 255, 255), (0, 0, 0), (0, 0, 225)


def initialize_grid():
    grid = np.zeros((ROWS, COLS), dtype=int)
    grid[1, 2] = grid[2, 3] = 1
    grid[3, 1:4] = 1
    return grid


def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for row in range(ROWS):
        for col in range(COLS):
            live_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    neighbor_row = (row + i) % ROWS
                    neighbor_col = (col + j) % COLS
                    live_neighbors += grid[neighbor_row, neighbor_col]

            if grid[row, col] == 1:
                if live_neighbors in (2, 3):
                    new_grid[row, col] = 1
            elif live_neighbors == 3:
                new_grid[row, col] = 1

    return new_grid


def draw_grid(screen, grid):
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            color = BLUE if grid[row, col] == 1 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    pygame.display.set_caption("Game of Life")

    grid = initialize_grid()
    running = True
    paused = False
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not paused:
            previous_grid = grid.copy()
            grid = update_grid(grid)

        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()
