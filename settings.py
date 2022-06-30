import numpy as np

class Settings:
    """Store settings for the game."""

    def __init__(self):
        """Initialize settings for game."""
    
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # Playable blob settings
        self.block_size = 50
        self.blob_color = (225,225,0)
        self.fps = 30



        # Playable map. Should be 16x16 (0 - 15)x(0 - 15)
        # 0 = Standard (no) tile. This has no affect. 
        # 1 = White (spawn) tile. The blob spawns here. There should only be one spawn tile.
        # 2 = Green (goal) tile. You win the game here and get positive points. There should only be one goal tile.
        # 3 = Red (lava) tile. This kills the blob and sends it back to spawn tile.
        # 4 = Blue (water) tile. This gives it negative points.
        self.map = np.array([[0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                             [0,1,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3],
                             [0,0,0,0,0,0,0,3,0,0,0,0,0,3,2,0],
                             [0,0,0,0,0,0,0,3,0,0,0,0,0,3,0,0],
                             [0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,0],
                             [999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
        
