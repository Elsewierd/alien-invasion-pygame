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
        self.ship = Ship(self)
    
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )   
        pg.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """
        Start the main loop for the game.
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pg.pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pg.pg.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pg.display.flip()


if __name__=="__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()