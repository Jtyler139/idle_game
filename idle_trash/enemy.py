import pygame
from shape import Shape
from constants import *

class Enemy(Shape):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), ENEMY_RADIUS, 2)
