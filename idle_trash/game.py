import pygame # type: ignore
from constants import *
import pygame.freetype # type: ignore


class Game:
    def __init__(self):
        pygame.init()
        pygame.freetype.init()
        pygame.display.set_caption("Idle Trash")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.current_state = None
        self.reset_timer_start = pygame.time.get_ticks()
        self.reset_delay_ms = 5000

    def set_state(self, new_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def run(self):
        running = True
        
        while running:
            dt = self.clock.tick(60)
            current_time = pygame.time.get_ticks()
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            if self.current_state:
                self.current_state.handle_events(events, current_time)
                self.current_state.update(dt)
                self.current_state.render(self.screen)
            
            pygame.display.flip()

            self.clock.tick(60)
        
        pygame.quit()
