import sys
import pygame as pg

from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """

    def __init__(self) -> None:
        """
        Initialize the game, and create the game resources
        """
        pg.init()
        self.settings = Settings()
    
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )   
        pg.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """
        Start the main loop for the game.
        """
        while True:
            # Watch for keyboard and mouse events.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            # Redraw the screen durring each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pg.display.flip()

if __name__=="__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()