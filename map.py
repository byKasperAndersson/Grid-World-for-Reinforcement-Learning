import pygame
import numpy as np

class Map:
    """Class for different tiles on map"""

    def __init__(self, blob_game):
        
        self.screen = blob_game.screen
        self.settings = blob_game.settings
        self.map = self.settings.map

    def add_tile(self, x_pos, y_pos, type_of_tile):
        self.rect = pygame.Rect(x_pos*self.settings.block_size, 
            y_pos*self.settings.block_size, self.settings.block_size, 
            self.settings.block_size)

        if type_of_tile == 1:
            self.color = (255,0,0)
        
        if type_of_tile == 2:
            self.color = (0,0,255)
        
        pygame.draw.rect(self.screen, self.color, self.rect)
        

    def draw_map(self):
        block_size = self.settings.block_size
        for x in range(self.settings.screen_height // block_size):
            for y in range(self.settings.screen_height // block_size):
                self.rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                type_of_tile = self.map[x,y]
                

                if type_of_tile == 1:
                    pygame.draw.rect(self.screen, (255,0,0), self.rect)
                if type_of_tile == 2:
                    pygame.draw.rect(self.screen, (0,0,255), self.rect)
        




      