import pygame # type: ignore
from shape import Shape
from constants import *

class Enemy(Shape):
    def __init__(self, x, y, color=WHITE):
        super().__init__(x, y, ENEMY_RADIUS)
        self.color = color
        self.mouse_over = False
        
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), ENEMY_RADIUS, 2)

    def update(self, dt):
        pass
