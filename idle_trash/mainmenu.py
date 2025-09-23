import pygame
from title import UIElement
from constants import *

class MainMenuState():
    def __init__():
        start_button = UIElement(
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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.quit_button.mouse_over:
                return "quit"
            if self.start_button.mouse_over:
                return "gameplay"