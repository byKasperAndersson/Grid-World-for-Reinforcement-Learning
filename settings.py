import numpy as np
import player_settings as ps

class Settings:
    """Store settings for the game. For adjustable game settings, 
        see file player_settings.py."""

    def __init__(self):
        """Initialize settings for game."""

        # Play yourself or start with Q_Learning.
        self.manual = ps.manual

        # Playable agent settings
        self.block_size = 80
        self.agent_color = (225,225,0)
        self.fps = 30
        
        # Screen settings
        self.screen_height = ps.map_to_play.shape[0]*self.block_size
        self.screen_width = ps.map_to_play.shape[1]*self.block_size
        self.screen_score_width = 300
        self.total_width =  self.screen_width + self.screen_score_width
        self.bg_color = (0,0,0)

        # Tile rewards. Format: [Standard, Spawn, Goal, Lava, Water]
        self.rewards = [0,0,10,-10,-1]

        # Game settings, map loaded etc. Most loaded from player_settings.py
        self.map = ps.map_to_play
        self.score = 0
        self.episodes = ps.episodes
        self.current_episode = 1
        self.q_table = np.zeros((self.map.shape[0], self.map.shape[1], 4))
        self.epsilon = ps.epsilon
        self.alpha = ps.alpha
        self.gamma = ps.gamma
