import pygame
from idle_trash.constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Idle Trash")

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
