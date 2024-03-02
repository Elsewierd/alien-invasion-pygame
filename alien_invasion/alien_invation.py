import sys
import pygame as pg

class AlienInvasion:
    """Overall class to manage game assets and behavior.
    """

    def __init__(self) -> None:
        """Initialize the game, and create the game resources
        """
        pg.init()
    
        self.screen = pg.display.set_mode((1200, 800))   
        pg.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """
        Start the main loop for the game.
        """
        while True:
            # Watch for keyboard and mouse events.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pg.display.flip()

if __name__=="__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()