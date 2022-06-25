import pygame 
import sys
from settings import Settings

class TheBlob:

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("The Blob")

    def run_game(self):
        """"Main loop of the game."""
        while True:
            self.update_screen()
            self.check_events()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        """Update images on screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == "__main__":
    # Make instance of game and run game.
    tb = TheBlob()
    tb.run_game()