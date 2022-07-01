import pygame

class Blob:
    """Playable character of the game."""

    def __init__(self, blob_game):

        # Load screen and settings of game
        self.screen = blob_game.screen
        self.settings = blob_game.settings
        self.color = self.settings.blob_color


        # Load image of blob charatcer
        # self.image = pygame.image.load("images\\blob.bmp")
        # self.rect = self.image.get_rect()
        
        self.rect = pygame.Rect(0, 0, self.settings.block_size, self.settings.block_size)


        # Start each new blob at position spawn tile from settings.
        for y in range(self.settings.screen_height // self.settings.block_size):
            for x in range(self.settings.screen_height // self.settings.block_size):
                if self.settings.map[y,x] == 1:
                    self.rect.topleft = (x*self.settings.block_size, y*self.settings.block_size)


        # Movment flags
        self.move_right = False
        self.move_left  = False
        self.move_up    = False
        self.move_down  = False

    def move_blob(self):

        if self.move_right and (self.rect.right < self.settings.screen_width):
            self.rect.x += self.settings.block_size
        if self.move_left and (self.rect.left > 0):
            self.rect.x -= self.settings.block_size
        if self.move_up and (self.rect.top > 0):
            self.rect.y -= self.settings.block_size
        if self.move_down and (self.rect.bottom < self.settings.screen_height):
            self.rect.y += self.settings.block_size

        #       # Movment flags
        # self.move_right = False
        # self.move_left  = False
        # self.move_up    = False
        # self.move_down  = False

        

    def draw_blob(self):
        """Function to draw the blob character on screen"""
        #self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)    


