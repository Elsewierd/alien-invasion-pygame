import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    """
    Overall class to manage game assets and behavior.
    """

    def __init__(self) -> None:
        """
        Initialize the game, and create the game resources
        """
        pg.init()
        self.settings = Settings()
        
        # sets windowed screen
        # self.screen = pg.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height)
        # )
        
        # sets fullscreen
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

        # asset instances
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self._create_fleet()

        pg.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """
        Start the main loop for the game.
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            # Always last update
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses.

        Args:
            event (pg.event): pygame keypress event
        """
        # right arrow
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        # left arrow
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        # spacebar
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        # 'q'
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responds to key releases.

        Args:
            event (pg.event): pygame key release event
        """
        # right arrow
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        # left arrow
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group
        """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Creates a fleet of aliens by populating self.aliens:Group
        """
        # New Alien instance
        alien = Alien(self)
        # Determine the number of aliens per row
        alien_width = alien.rect.width
        availble_space_x = self.settings.screen_width - (2 * alien_width)
        aliens_per_row = availble_space_x // (2 * alien_width)
        # Create a row of aliens
        for alien_number in range(aliens_per_row):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            # Add to Group
            self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pg.display.flip()


if __name__=="__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()