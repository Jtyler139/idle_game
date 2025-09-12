import pygame # type: ignore
from constants import *
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Idle Trash")

    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 255))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
