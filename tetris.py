import pygame
import random

# Játékablak beállításai
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
FPS = 10

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Tetrominók és azok színei
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]
SHAPES_COLORS = [CYAN, YELLOW, MAGENTA, RED, GREEN, BLUE, ORANGE]

# Kezdőpont
START_X, START_Y = 3, 0

# Inicializálás
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))


def draw_tetromino(shape, color, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, (x + j * GRID_SIZE, y + i * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def move_tetromino(shape, x, y):
    new_shape = []
    for i, row in enumerate(shape):
        new_row = []
        for j, cell in enumerate(row):
            if cell:
                new_row.append((x + j, y + i))
        new_shape.append(new_row)
    return new_shape


def check_collision(shape, x, y, grid):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if x + j < 0 or x + j >= WIDTH // GRID_SIZE or y + i >= HEIGHT // GRID_SIZE or grid[y + i][x + j] != 0:
                    return True
    return False


def clear_lines(grid):
    full_rows = [i for i, row in enumerate(grid) if all(cell != 0 for cell in row)]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * (WIDTH // GRID_SIZE))
    return len(full_rows)


def main():
    grid = [[0] * (WIDTH // GRID_SIZE) for _ in range(HEIGHT // GRID_SIZE)]
    current_tetromino = random.choice(SHAPES)
    current_color = random.choice(SHAPES_COLORS)
    x, y = START_X, START_Y
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_x = x - 1
            if not check_collision(current_tetromino, new_x, y, grid):
                x = new_x
        if keys[pygame.K_RIGHT]:
            new_x = x + 1
            if not check_collision(current_tetromino, new_x, y, grid):
                x = new_x
        if keys[pygame.K_DOWN]:
            new_y = y + 1
            if not check_collision(current_tetromino, x, new_y, grid):
                y = new_y

        if keys[pygame.K_SPACE]:
            rotated_tetromino = list(zip(*reversed(current_tetromino)))
            if not check_collision(rotated_tetromino, x, y, grid):
                current_tetromino = rotated_tetromino

        # Frissítsük az ablakot
        screen.fill(BLACK)
        draw_grid()

        # Kirajzoljuk a rácselemeket a megfelelő színnel
        for i, row in enumerate(grid):
            for j, cell_color in enumerate(row):
                if cell_color:
                    pygame.draw.rect(screen, cell_color, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        draw_tetromino(current_tetromino, current_color, x * GRID_SIZE, y * GRID_SIZE)

        if not check_collision(current_tetromino, x, y + 1, grid):
            y += 1
        else:
            # Tetromino leesett, rögzítés a rácsban
            for i, row in enumerate(current_tetromino):
                for j, cell in enumerate(row):
                    if cell:
                        grid[y + i][x + j] = current_color  # Szín rögzítése a rácsban

            lines_cleared = clear_lines(grid)
            score += lines_cleared * 100

            # Új tetromino
            current_tetromino = random.choice(SHAPES)
            current_color = random.choice(SHAPES_COLORS)
            x, y = START_X, START_Y

            # Ha nem fér el az új tetromino a kezdőpozíción, a játék véget ér
            if check_collision(current_tetromino, x, y, grid):
                print("Game Over!")
                pygame.quit()
                quit()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()