import pygame 
import sys
from settings import Settings
from blob import Blob

class The_Blob:

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("The Blob")
        self.blob = Blob(self)


    def run_game(self):
        """"Main loop of the game."""
        while True:
            self.check_events()
            self.update_screen()
            self.blob.move_blob()

            # For every second, at most "self.fps" frames may pass.
            clock = pygame.time.Clock()
            clock.tick(self.settings.fps)


    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.blob.move_right = True
                if event.key == pygame.K_LEFT:
                    self.blob.move_left = True
                if event.key == pygame.K_UP:
                    self.blob.move_up = True
                if event.key == pygame.K_DOWN:
                    self.blob.move_down = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.blob.move_right = False
                if event.key == pygame.K_LEFT:
                     self.blob.move_left = False
                if event.key == pygame.K_UP:
                    self.blob.move_up = False
                if event.key == pygame.K_DOWN:
                    self.blob.move_down = False

    def update_screen(self):
        """Update images on screen and flip to new screen."""
        pygame.display.update() # update() is same as flip without any arguments
        self.screen.fill(self.settings.bg_color)
        self.draw_grid()
        self.blob.draw_blob()


    def draw_grid(self):
        """Draw background grid"""
        block_size = self.settings.block_size
        for x in range(self.settings.screen_height // block_size):
            for y in range(self.settings.screen_height // block_size):
                # Create a rect at position (x,y)*blocksize with the size of blocksize^2
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                # Draw the rectangle on screen, with color 200^3, and with bordersize of 1
                pygame.draw.rect(self.screen, (200,200,200), rect, 1)


if __name__ == "__main__":
    # Make instance of game and run game.
    blob_game = The_Blob()
    blob_game.run_game()