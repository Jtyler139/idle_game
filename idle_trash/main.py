import pygame # type: ignore
from constants import *
import sys
from enemy import Enemy
from title import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    uielement = UIElement(
        center_position=(screen_width//2, screen_height//4),
        font_size=30,
        bg_rgb=(106, 159, 181),
        text_rgb=(255, 255, 255),
        text='Start Game'
    )

    quit_button = UIElement(
        center_position=(screen_width//2, screen_height * 0.75),
        font_size=20,
        bg_rgb=(106, 159, 181),
        text_rgb=(255,255,255),
        text='Quit'
    )

    pygame.display.set_caption("Idle Trash")

    clock = pygame.time.Clock()

    new_enemy = Enemy(screen_width//2, screen_height//2)

    #updateable = pygame.sprite.Group()
    #drawable = pygame.sprite.Group()

    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.mouse_over:
                    running = False

        screen.fill((106, 159, 181))

        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        quit_button.update(pygame.mouse.get_pos())
        quit_button.draw(screen)

        
        new_enemy.draw(screen)

        pygame.display.flip()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
