import pygame

class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super.__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass