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

        # Start each new blob at position 
        self.rect.topleft = (0,0)

    def draw_blob(self):
        """Function to draw the blob character on screen"""
        #self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)    


