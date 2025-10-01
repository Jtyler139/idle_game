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
        current_health_width = self.width * self.health_ratio
        pygame.draw.rect(surface, RED, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, GREEN, (self.x, self.y, current_health_width, self.height))

    def update(self, dt):
        pass

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)
        self.health_ratio = self.current_hp / self.max_hp

    def reset_enemy(self):
        self.current_hp = self.max_hp
        self.health_ratio = self.current_hp / self.max_hp
