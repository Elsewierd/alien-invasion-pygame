import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A classs to manage bullets fired from the ship."""
    def __init__(self, ai_game):
        """Creates a bullet object at the ships current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Stores the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
    def update(self):
        """Moves the bullet up the screen"""
        # Update the bullet's position
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen
        """
        pg.draw.rect(self.screen, self.color, self.rect)