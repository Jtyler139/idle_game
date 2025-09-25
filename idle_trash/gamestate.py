import pygame # type: ignore
from constants import *
from game import Game
from button import UIElement

class GameState:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        pass
    def update(self, dt):
        pass
    def render(self, screen):
        pass
    def enter(self):
        pass
    def exit(self):
        pass

class MainMenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.start_button = UIElement(
        center_position=(screen_width//2, screen_height//4),
        font_size=30,
        bg_rgb=(106, 159, 181),
        text_rgb=(255, 255, 255),
        text='Start Game'
        )
        self.buttons = [self.start_button]

        self.quit_button = UIElement(
        center_position=(screen_width//2, screen_height * 0.75),
        font_size=20,
        bg_rgb=(106, 159, 181),
        text_rgb=(255,255,255),
        text='Quit'
        )

    def enter(self):
        print("Welcome to Idle Trash")

    def start_game(self):
        print("Starting game...")
        self.game.set_state(GameplayState(self.game))
        

    def exit_game(self):
        print("Exiting game...")
        pygame.quit()
        import sys
        sys.exit()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.mouse_over:
                    self.start_game()
                    
                if self.quit_button.mouse_over:
                    self.exit_game()
                
    def render(self, screen):
        screen.fill(BLUE)
        self.start_button.draw(screen)
        self.quit_button.draw(screen)

    def update(self, dt):
        self.start_button.update(pygame.mouse.get_pos())
        self.quit_button.update(pygame.mouse.get_pos())

class GameplayState(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, game):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((255,255,255))