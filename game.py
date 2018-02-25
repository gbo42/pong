import pygame
import random
import sys
from core import *

# game settings
HEIGHT = 400
WIDTH = 600
lineW = 10
finished = False
scored = True

# game objects
leftPaddle = Paddle(30, HEIGHT/2, 20, 100)
rightPaddle = Paddle(WIDTH - 50, HEIGHT/2, 20, 100)
ball = Ball(WIDTH/2, HEIGHT/2, 20)

# pygame setup
pygame.init()
pygame.key.set_repeat(10, 10)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.Font('Square.ttf', 100)

# controls
def keyP():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        global finished
        finished = True
    if keys[pygame.K_s]:
        leftPaddle.move(clock.get_time() * 1, HEIGHT)
    if keys[pygame.K_w]:
        leftPaddle.move(clock.get_time() * -1, HEIGHT)
    if keys[pygame.K_DOWN]:
        rightPaddle.move(clock.get_time() * 1, HEIGHT)
    if keys[pygame.K_UP]:
        rightPaddle.move(clock.get_time() * -1, HEIGHT)


# main loop
while not finished:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and scored:
                scored = False
                ball.start()

    # call key control handler
    keyP()

    # game logic
    ball.collide((leftPaddle,rightPaddle), HEIGHT)
    ball.move(clock.get_time())
    scorer = ball.endCheck(WIDTH)

    if scorer != 0 and not scored:
        scored = True
        if scorer == 1:
            leftPaddle.points += 1
        elif scorer == -1:
            rightPaddle.points += 1

    # render
    screen.fill(BLACK)
    drawScore(font, leftPaddle, rightPaddle, screen, WIDTH)
    leftPaddle.draw(screen)
    rightPaddle.draw(screen)
    ball.draw(screen)
    drawBoard(screen, 20, HEIGHT, WIDTH)
    pygame.display.flip()
    clock.tick()

# exit game
pygame.quit()
