import pygame
from random import randrange

res = 800
size = 50

x, y = randrange(0, res, size), randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5
pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
front_score = pygame.font.SysFont('Arial', 22, bold=True)
front_end = pygame.font.SysFont('Arial', 28, bold=True)


while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('blue'), (i, j, size - 2, size - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))
    render_score = front_score.render(f'Score: {score}', 1, pygame.Color('white'))
    sc.blit(render_score, (5, 5))
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = randrange(0, res, size), randrange(0, res, size)
        lenght += 1
        score += 1
        fps += 1
    if x < 0 or x > res - size or y < 0 or y > res - size or len(snake) != len(set(snake)):
        while True:
            render_end = front_end.render('GAME OVER', 1, pygame.Color('red'))
            sc.blit(render_end, (res // 2 - 200, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}