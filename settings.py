
class Settings:
    """Store settings for the game"""

    def __init__(self):

        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # Playable blob settings
        self.block_size = 50
        self.blob_color = (0,225,0)
        self.fps = 30
        
