import sys
import pygame
import random
from core import *

HEIGHT = 600
WIDTH = 1200
lineW = 10


def drawBorder(borderSize):
    pygame.draw.rect(screen, WHITE, [0, 0, borderSize, HEIGHT])
    # pygame.draw.rect(screen, WHITE, [0, 0, WIDTH, borderSize])
    # pygame.draw.rect(screen, WHITE, [0, HEIGHT-borderSize, WIDTH, borderSize])
    pygame.draw.rect(screen, WHITE, [WIDTH-borderSize, 0, borderSize, HEIGHT])


# game objects and settings
finished = False
leftPaddle = Paddle(30, HEIGHT/2, 20, 100)
ball = Ball(WIDTH/2, HEIGHT/2, 20)

# custom event
MYEVENT = pygame.USEREVENT+1

# pygame setup
pygame.init()
pygame.key.set_repeat(10, 10)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# main loop
while not finished:
    screen.fill((0,0,0))
    leftPaddle.draw(screen)
    drawBorder(20)
    ball.draw(screen)
    print(clock.get_time())
    ball.move(clock.get_time())
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            if event.key == pygame.K_DOWN:
                leftPaddle.move(1, HEIGHT)
            if event.key == pygame.K_UP:
                leftPaddle.move(-1, HEIGHT)

    # render
    pygame.display.flip()
    clock.tick()

# exit game
pygame.quit()
