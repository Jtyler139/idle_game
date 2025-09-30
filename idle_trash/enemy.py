import pygame # type: ignore
from shape import Shape
from constants import *
import math

class Enemy(Shape):
    def __init__(self, x, y, color=WHITE):
        super().__init__(x, y, ENEMY_RADIUS)
        self.color = color
        self.mouse_over = False
        
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), ENEMY_RADIUS, 2)

    def update(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        distance = math.sqrt((mouse_x - self.x)**2 + (mouse_y - self.y)**2)
        if distance <= ENEMY_RADIUS:
            self.mouse_over = True
        else:
            self.mouse_over =  False
        
