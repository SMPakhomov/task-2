import pygame
import random

pygame.init()

MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 10)


def draw(screen, pos, r, color):
    pygame.draw.circle(screen, color, pos, r)


pygame.init()
size = width, height = 600, 600
running = True
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))
pos = (random.randint(1, 600), random.randint(0, 600))
color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
r = random.randint(1, 50)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(pygame.Color('blue'))
            r = 1
            draw(screen, event.pos, r)
            pos = event.pos
            pygame.time.set_timer(MYEVENTTYPE, 10)
        if event.type == MYEVENTTYPE:
            draw(screen, pos, r, color)
            pos = (random.randint(1, 600), random.randint(0, 600))
            r = random.randint(1, 50)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.display.flip()
