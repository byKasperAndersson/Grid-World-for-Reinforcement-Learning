import pygame


class Agent:
    """Playable character of the game and it's movements."""

    def __init__(self, grid_world):

        # Load screen and settings of game
        self.screen = grid_world.screen
        self.settings = grid_world.settings
        self.score = grid_world.score
        self.color = self.settings.agent_color
        self.map = grid_world.map
        self.spawn_tile = grid_world.spawn_tile
        self.grid_world = grid_world


        # Load image of agent charatcer
        # self.image = pygame.image.load("images\\agent.bmp")
        # self.rect = self.image.get_rect()
        
        self.rect = pygame.Rect(0, 0, self.settings.block_size, self.settings.block_size)


        # Start each new agent at position spawn tile from settings.
        for y in range(self.settings.screen_height // self.settings.block_size):
            for x in range(self.settings.screen_height // self.settings.block_size):
                if self.settings.map[y,x] == 1:
                    self.rect.topleft = (x*self.settings.block_size, y*self.settings.block_size)


        # Movment flags
        self.move_right = False
        self.move_left  = False
        self.move_up    = False
        self.move_down  = False

    def move_agent(self, manual, algorithm_movement = None):
        """Moves the agent according to either keyboard arrows (manual = True) or 
            from Q-Learning algorithm (manual = False).
            If manual = False, then algorithm_movement should be the new position
            of the agent (= [x_new,y_new])."""

        if manual:
            if self.move_right and (self.rect.right < self.settings.screen_width):
                self.rect.x += self.settings.block_size
                self.detect_collision(game = self.grid_world)
            if self.move_left and (self.rect.left > 0):
                self.rect.x -= self.settings.block_size
                self.detect_collision(game = self.grid_world)
            if self.move_up and (self.rect.top > 0):
                self.rect.y -= self.settings.block_size
                self.detect_collision(game = self.grid_world)
            if self.move_down and (self.rect.bottom < self.settings.screen_height):
                self.rect.y += self.settings.block_size
                self.detect_collision(game = self.grid_world)
        else:
            self.rect.x = algorithm_movement[0]*self.settings.block_size
            self.rect.y = algorithm_movement[1]*self.settings.block_size
            self.detect_collision(game = self.grid_world)


    def draw_agent(self):
        """Function to draw the agent character on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def detect_collision(self, game):
        """Detects collisions and calls proper collision function."""
        block_size = self.settings.block_size

        for tile in self.map.tiles:
            if [self.rect.x // block_size, self.rect.y // block_size] == [tile[1].x, tile[1].y]:
                
                # Green (goal) collision, send back to spawn, positive points.
                if tile[0] == 2:
                    self.goal_collision(game)
                    game.current_episode += 1

                # Red (lava) collision, send back to spawn, negative points.
                if tile[0] == 3:
                    self.lava_collision(game)
                    game.current_episode += 1

                # Blue (water) collision, negative points.
                if tile[0] == 4:
                    self.water_collision(game)


    def goal_collision(self, game):
        self.rect.topleft = [self.settings.block_size*i for i in self.spawn_tile]
        game.score = round(game.score + self.settings.rewards[2],3)
        #print("Goal Collision")

    def lava_collision(self, game):
        self.rect.topleft = [self.settings.block_size*i for i in self.spawn_tile]
        game.score = round(game.score + self.settings.rewards[3],3)
        #print("Lava Collision")

    def water_collision(self, game):
        #Implement when QL is done.
        game.score = round(game.score + (self.settings.rewards[4])/2,3)
        #print("Water Collision")


