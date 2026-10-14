import pygame
import random
import sys


pygame.init()

size = 30
cols = 10
rows = 20
screen = pygame.display.set_mode((cols * size + 160, rows * size))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)
pygame.key.set_repeat(200, 60)

shapes = {
    "I": [(-1, 0), (0, 0), (1, 0), (2, 0)],
    "O": [(0, 0), (1, 0), (0, 1), (1, 1)],
    "T": [(-1, 0), (0, 0), (1, 0), (0, 1)],
    "S": [(0, 0), (1, 0), (-1, 1), (0, 1)],
    "Z": [(-1, 0), (0, 0), (0, 1), (1, 1)],
    "J": [(-1, 0), (0, 0), (1, 0), (-1, 1)],
    "L": [(-1, 0), (0, 0), (1, 0), (1, 1)],
}

colors = {
    "I": (0, 240, 240),
    "O": (240, 240, 0),
    "T": (160, 0, 240),
    "S": (0, 240, 0),
    "Z": (240, 0, 0),
    "J": (0, 0, 240),
    "L": (240, 160, 0),
}


def new_board():
    b = []
    for i in range(rows):
        b.append([0] * cols)
    return b


def fits(shape, px, py):
    for x, y in shape:
        nx = px + x
        ny = py + y
        if nx < 0 or nx >= cols or ny >= rows:
            return False
        if ny >= 0 and board[ny][nx] != 0:
            return False
    return True


def rotate(shape):
    new = []
    for x, y in shape:
        new.append((-y, x))
    return new


def new_piece():
    name = random.choice(list(shapes.keys()))
    return name, shapes[name], 4, 0


def write(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


board = new_board()
name, shape, px, py = new_piece()
score = 0
lines = 0
dead = False
timer = 0

while True:
    timer += clock.tick(60)

    level = lines // 10
    delay = 500 - level * 40
    if delay < 100:
        delay = 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if dead:
                if event.key == pygame.K_r:
                    board = new_board()
                    name, shape, px, py = new_piece()
                    score = 0
                    lines = 0
                    dead = False
                continue

            if event.key == pygame.K_LEFT and fits(shape, px - 1, py):
                px -= 1
            if event.key == pygame.K_RIGHT and fits(shape, px + 1, py):
                px += 1
            if event.key == pygame.K_DOWN and fits(shape, px, py + 1):
                py += 1
            if event.key == pygame.K_UP and name != "O":
                r = rotate(shape)
                if fits(r, px, py):
                    shape = r
            if event.key == pygame.K_SPACE:
                while fits(shape, px, py + 1):
                    py += 1
                timer = delay

    if not dead and timer >= delay:
        timer = 0

        if fits(shape, px, py + 1):
            py += 1
        else:
            for x, y in shape:
                board[py + y][px + x] = colors[name]

            left = []
            for row in board:
                if 0 in row:
                    left.append(row)
            cleared = rows - len(left)
            for i in range(cleared):
                left.insert(0, [0] * cols)
            board = left

            lines += cleared
            if cleared == 1:
                score += 100
            elif cleared == 2:
                score += 300
            elif cleared == 3:
                score += 500
            elif cleared == 4:
                score += 800

            name, shape, px, py = new_piece()
            if not fits(shape, px, py):
                dead = True

    screen.fill((0, 0, 0))

    for x in range(cols + 1):
        pygame.draw.line(screen, (40, 40, 40), (x * size, 0), (x * size, rows * size))
    for y in range(rows + 1):
        pygame.draw.line(screen, (40, 40, 40), (0, y * size), (cols * size, y * size))

    for y in range(rows):
        for x in range(cols):
            if board[y][x] != 0:
                pygame.draw.rect(screen, board[y][x], (x * size, y * size, size - 1, size - 1))

    if not dead:
        for x, y in shape:
            pygame.draw.rect(screen, colors[name], ((px + x) * size, (py + y) * size, size - 1, size - 1))

    write("Score", cols * size + 20, 40)
    write(str(score), cols * size + 20, 70)
    write("Lines", cols * size + 20, 130)
    write(str(lines), cols * size + 20, 160)
    write("Level", cols * size + 20, 220)
    write(str(level), cols * size + 20, 250)

    if dead:
        write("GAME OVER", 60, rows * size // 2 - 20)
        write("Press R", 85, rows * size // 2 + 20)

    pygame.display.update()
