import pygame
import random
import sys

pygame.init()

size = 20
w = 30
h = 20
screen = pygame.display.set_mode((w * size, h * size))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

snake = [(10, 10), (9, 10), (8, 10)]
dx = 1
dy = 0
score = 0
dead = False


def get_food():
    while True:
        f = (random.randint(0, w - 1), random.randint(0, h - 1))
        if f not in snake:
            return f


food = get_food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx = 0
                dy = -1
            if event.key == pygame.K_DOWN and dy != -1:
                dx = 0
                dy = 1
            if event.key == pygame.K_LEFT and dx != 1:
                dx = -1
                dy = 0
            if event.key == pygame.K_RIGHT and dx != -1:
                dx = 1
                dy = 0
            if event.key == pygame.K_r and dead:
                snake = [(10, 10), (9, 10), (8, 10)]
                dx = 1
                dy = 0
                score = 0
                dead = False
                food = get_food()

    if not dead:
        head = ((snake[0][0] + dx) % w, (snake[0][1] + dy) % h)

        if head in snake:
            dead = True
        else:
            snake.insert(0, head)
            if head == food:
                score += 1
                food = get_food()
            else:
                snake.pop()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (220, 0, 0), (food[0] * size, food[1] * size, size, size))

    for i in range(len(snake)):
        if i == 0:
            color = (0, 220, 0)
        else:
            color = (0, 130, 0)
        pygame.draw.rect(screen, color, (snake[i][0] * size, snake[i][1] * size, size - 1, size - 1))

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if dead:
        text = font.render("Game over! Press R to restart", True, (255, 255, 255))
        screen.blit(text, (w * size // 2 - 150, h * size // 2))

    pygame.display.update()
    clock.tick(10)
