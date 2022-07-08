import pygame


class Blob:
    """Playable character of the game and it's movements."""

    def __init__(self, blob_game):

        # Load screen and settings of game
        self.screen = blob_game.screen
        self.settings = blob_game.settings
        self.score = blob_game.score
        self.color = self.settings.blob_color
        self.map = blob_game.map
        self.spawn_tile = blob_game.spawn_tile
        self.blob_game = blob_game


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

    def move_blob(self, manual, algorithm_movement = None):
        """Moves the blob according to either keyboard arrows (manual = True) or 
            from Q-Learning algorithm (manual = False).
            If manual = False, then algorithm_movement should be the new position
            of the blob (= [x_new,y_new])."""

        if manual:
            if self.move_right and (self.rect.right < self.settings.screen_width):
                self.rect.x += self.settings.block_size
                self.detect_collision(game = self.blob_game)
            if self.move_left and (self.rect.left > 0):
                self.rect.x -= self.settings.block_size
                self.detect_collision(game = self.blob_game)
            if self.move_up and (self.rect.top > 0):
                self.rect.y -= self.settings.block_size
                self.detect_collision(game = self.blob_game)
            if self.move_down and (self.rect.bottom < self.settings.screen_height):
                self.rect.y += self.settings.block_size
                self.detect_collision(game = self.blob_game)
        else:
            self.rect.x = algorithm_movement[0]*self.settings.block_size
            self.rect.y = algorithm_movement[1]*self.settings.block_size
            self.detect_collision(game = self.blob_game)


    def draw_blob(self):
        """Function to draw the blob character on screen"""
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
        game.score = round(game.score + self.settings.rewards[4],3)
        #print("Water Collision")


