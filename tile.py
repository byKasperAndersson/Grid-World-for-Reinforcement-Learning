import pygame

class Tile:
    """Class for different tiles on map"""

    def __init__(self, blob_game, x_pos, y_pos, type_of_tile):

        self.screen = blob_game.screen
        self.settings = blob_game.settings
        self.rect = pygame.Rect(x_pos, y_pos, self.settings.block_size, self.settings.block_size)

    
    def lava_tile(self):
        print()


        