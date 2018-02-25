import sys
import pygame
import math

WHITE = (255, 255, 255)

class Ball:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.dir = (0, 1)
        self.speed = 0.4

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x - self.d/2, self.y - self.d/2, self.d, self.d])

    def move(self, tick):
        self.x += self.dir[0] * self.speed * tick
        self.y += self.dir[1] * self.speed * tick

class Paddle:
    def __init__(self, x, y, w, h):
        self.movSpeed = 10
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y - self.h/2, self.w, self.h])

    def move(self, y, H):
        if self.y + (self.movSpeed*y) + self.h/2 > H:
            self.y = H - self.h/2
        elif self.y + (self.movSpeed*y) - self.h/2 < 0:
            self.y = self.h/2
        else:
            self.y += self.movSpeed * y
