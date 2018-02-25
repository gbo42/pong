import sys
import pygame
import math
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Ball:
    def __init__(self, x, y, d):
        self.startx = x
        self.x = x
        self.starty = y
        self.y = y
        self.d = d
        self.dir = (0, 0)
        self.speed = 0.4

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.x - self.d/2, self.y - self.d/2, self.d, self.d])

    def move(self, tick):
        self.x += self.dir[0] * self.speed * tick
        self.y += self.dir[1] * self.speed * tick

    def collide(self, paddles, h):
        if self.y + 10 >= h:
            self.y = h - 11
            self.dir = (self.dir[0], -self.dir[1])
        if self.y - 10 <= 0:
            self.y = 11
            self.dir = (self.dir[0], -self.dir[1])

        for paddle in paddles:
            if self.x + 10 >= paddle.x and self.x - 10 <= paddle.x+paddle.w:
                if self.y + 10 >= paddle.y - paddle.h/2 and self.y - 10 <= paddle.y+paddle.h/2:
                    xdir = (self.dir[0] + self.x - paddle.y) * - 1
                    ydir = self.dir[1] + (self.y - paddle.y)
                    magnitude = math.sqrt(xdir*xdir + ydir * ydir)
                    self.dir = (xdir/magnitude, ydir/magnitude)

    def endCheck(self, W):
        if self.x >= W:
            return 1
        elif self.x <= 0:
            return -1
        else:
            return 0

    def start(self):
        self.x = self.startx
        self.y = self.starty
        xdir = -1 if random.random() >= 0.5 else 1
        self.dir = (xdir, 0)

class Paddle:
    def __init__(self, x, y, w, h):
        self.movSpeed = 0.5
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.points = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y - self.h/2, self.w, self.h])

    def move(self, y, H):
        if self.y + (self.movSpeed*y) + self.h/2 > H:
            self.y = H - self.h/2
        elif self.y + (self.movSpeed*y) - self.h/2 < 0:
            self.y = self.h/2
        else:
            self.y += self.movSpeed * y

def drawBoard(screen, borderSize, HEIGHT, WIDTH):
    pygame.draw.rect(screen, WHITE, [0, 0, borderSize, HEIGHT])
    pygame.draw.rect(screen, WHITE, [WIDTH-borderSize, 0, borderSize, HEIGHT])
    h = 10
    for i in range(int(HEIGHT/h)):
        pygame.draw.rect(screen, WHITE, [WIDTH/2-h/2, i*(h*2)-5, h, h])

def drawScore(font, leftPaddle, rightPaddle, screen, WIDTH):
    textL = str(leftPaddle.points)
    textR = str(rightPaddle.points)
    textsurfaceL = font.render(textL, True, WHITE)
    screen.blit(textsurfaceL,(WIDTH/2 - font.size(textL)[0] - 100,0))
    textsurfaceR = font.render(textR, True, WHITE)
    screen.blit(textsurfaceR,(WIDTH/2 + 100,0))
