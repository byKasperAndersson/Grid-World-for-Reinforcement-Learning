import numpy as np

class Settings:
    """Store settings for the game."""

    def __init__(self):
        """Initialize settings for game."""

        # True == play manual 
        # False == Q-learning
        self.manual = False
        
        # Screen settings
        self.screen_width = 500
        self.screen_score_width = 300
        self.total_width =  self.screen_width + self.screen_score_width
        self.screen_height = 500
        self.bg_color = (0,0,0)

        # Playable blob settings
        self.block_size = 50
        self.blob_color = (225,225,0)
        self.fps = 30

        # Tile rewards. Format: [Standard, Spawn, Goal, Lava, Water]
        self.rewards = [0,0,10,-10,-2]

        # Playable map. Should be 16x16 (0 - 15)x(0 - 15)
        # 0 = Standard (no) tile. This has no affect. 
        # 1 = White (spawn) tile. The blob spawns here. There should only be one spawn tile.
        # 2 = Green (goal) tile. You win the game here and get positive points. There should only be one goal tile.
        # 3 = Red (lava) tile. This kills the blob and sends it back to spawn tile.
        # 4 = Blue (water) tile. This gives it negative points.

        #16x16 map
        # self.map = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0],
        #                      [4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0],
        #                      [4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0],
        #                      [4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

        #10x10 map
        self.map = np.array([[0,0,0,0,0,0,0,0,0,0],
                             [0,1,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,3,0,0,0,0,0],
                             [0,0,0,0,3,0,0,0,0,0],
                             [0,0,0,0,3,0,0,0,0,0],
                             [0,0,0,0,3,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,2,0],
                             [0,0,0,0,0,0,0,0,0,0]])
        
