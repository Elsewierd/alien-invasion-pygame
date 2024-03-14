import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet
    """

    def __init__(self, ai_game):
        """Initailize the alien, and its settings

        Args:
            ai_game (AlienInvasion): Overall game object
        """

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute
        self.image = pg.image.load('./alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        """Returns True if alien is at the edge of the screen
        """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien based on fleet_direction
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
