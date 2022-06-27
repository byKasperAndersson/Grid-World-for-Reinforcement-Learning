import pygame
import numpy as np

class Map:
    """Class for different tiles on map"""

    def __init__(self, blob_game):

        self.screen = blob_game.screen
        self.settings = blob_game.settings
        self.map = np.zeros((self.settings.screen_height // self.settings.block_size,
            self.settings.screen_weight // self.settings.screen_height))

    def add_tile(self, x_pos, y_pos, type_of_tile):
        self.rect = pygame.Rect(x_pos, y_pos, self.settings.block_size, self.settings.block_size)
        
        # Lava tile
        if type_of_tile == 1:
            self.color = (255,0,0)
            pygame.draw.rect(self.screen, self.color, self.rect)

        




        