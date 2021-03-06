import pygame


class Map:
    """Class for different tiles on map"""
    """Design of playable maps is found in player_settings.py"""

    def __init__(self, grid_game):
        
        self.screen = grid_game.screen
        self.settings = grid_game.settings
        self.map = self.settings.map
        self.tiles = []

    # Used for testing
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
        """"Comment"""
        block_size = self.settings.block_size
        for x in range(self.settings.screen_width// block_size):
            for y in range(self.settings.screen_height // block_size):
                self.rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                type_of_tile = self.map[y,x]

                if type_of_tile == 1: # White (spawn)
                    pygame.draw.rect(self.screen, (255,255,255), self.rect)
                if type_of_tile == 2: # Green (win)
                    pygame.draw.rect(self.screen, (0,255,0), self.rect)
                if type_of_tile == 3: # Red (lava)
                    pygame.draw.rect(self.screen, (255,0,0), self.rect)
                if type_of_tile == 4: # Blue (water)
                    pygame.draw.rect(self.screen, (0,0,255), self.rect)

    def create_map_rects(self, return_spawn_tile = False):
        """Create rects for non-zero tiles on maps. Also gives option to return spawn tile."""
        block_size = self.settings.block_size
        for x in range(self.settings.screen_width // block_size):
            for y in range(self.settings.screen_height // block_size):
                type_of_tile = self.map[y,x]

                if type_of_tile != 0:
                    tile = pygame.Rect(x, y, block_size, block_size)
                    self.tiles.append([type_of_tile, tile])

                    if type_of_tile == 1:
                        spawn_tile = [x,y]

        if return_spawn_tile:
            return(spawn_tile)


                    
                    


        




      