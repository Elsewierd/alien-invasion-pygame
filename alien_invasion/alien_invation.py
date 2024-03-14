import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    """Overall class to manage game assets and behavior.
    """

    def __init__(self) -> None:
        """Initialize the game, and create the game resources
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
        """Start the main loop for the game.
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()

            self._update_aliens()

            # Always last update
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events.
        """
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

    def _check_fleet_edges(self):
        """Responds if any alien reaches an edge
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group
        """

        if len(self.bullets) < self.settings.bullets_allowed:

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collisions(self):
        """Responds to bullet-alien collisions
        """
        # Remove any bullets and aliens that collided
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_bullets(self):
        """Updates the position of bullets, removes the bullets that have exited the screen
        """
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Check for bullet and alien collision, removing both if true
        self._check_bullet_alien_collisions()
        
    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row

        Args:
            alien_number (int): the number of the alien created from left to right
            row_number (int): the number of the row the alien created in from top
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Creates a fleet of aliens
        """
        # New Alien instance
        alien = Alien(self)
        # Determine the number of aliens per row
        alien_width, alien_height = alien.rect.size
        availble_space_x = self.settings.screen_width - (2 * alien_width)
        aliens_per_row = availble_space_x // (2 * alien_width)
        # Determine the number of possible rows
        ship_height = self.ship.rect.height
        availble_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = availble_space_y // (2 * alien_height)
        # Create a row of aliens
        for row_number in range(number_rows):
            for alien_number in range(aliens_per_row):
                self._create_alien(alien_number, row_number)

    def _update_aliens(self):
        """Checks if the fleet is at the edge, updates the positions of all the aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.
        """
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