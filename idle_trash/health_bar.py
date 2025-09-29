import pygame # type: ignore
from constants import *

class HealthBar:
    def __init__(self, x, y, current_hp, max_hp, width, height):
        self.x = x
        self.y = y
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.width = width
        self.height = height
        self.health_ratio = current_hp / max_hp

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.width, self.height))
        current_health_width = self.width * self.health_ratio
        pygame.draw.rect(surface, GREEN, (self.x, self.y, current_health_width, self.height))