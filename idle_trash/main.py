import pygame # type: ignore
from constants import *
import sys
from enemy import Enemy
from button import *
from game import Game
from gamestate import MainMenuState, GameState, GameplayState

def main():
    game = Game()
    game.set_state(MainMenuState(game))
    game.run()


if __name__ == "__main__":
    main()
    
