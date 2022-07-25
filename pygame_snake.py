import pygame
import random

size =25
key = (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT)
snake = [random.choices(range(size), k=2)]
food = random.choices(range(size), k=2)
screen = pygame.display.set_mode((size ** 2, size ** 2))
keys = pygame.K_RIGHT
running = True

pygame.init()
while running:
    pygame.time.Clock().tick(20)
    screen.fill((0, 0, 0))
    for segment in snake:
        values = (segment[0] * size, segment[1] * size, size, size)
        pygame.draw.rect(screen, (0,255, 0), values)
    values =  (food[0]  * size, food[1] * size, size, size)
    pygame.draw.rect(screen, (255, 0, 0), values)
    pygame.display.update()

    head = snake[-1][:]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in keys:
            key = event.key
    if key == pygame.K_UP:
        head[1] = (head[1] - 1 + size) % size
    elif key == pygame.K_LEFT:
        head[0] = (head[0] - 1) + size % size
    elif key == pygame.K_RIGHT:
        head[1] = (head[1] + 1) % size
    elif key == pygame.K_RIGHT:
        head[0] = (head[0] + 1) % size

    if head in snake:
        snake = [random.choices(range(size), k=2)]
    else:
        snake.append(head)
        if head == food:
            food = random.choices(range(size), k=2)
        else:
            snake.pop(0)
pygame.quit()
        
    