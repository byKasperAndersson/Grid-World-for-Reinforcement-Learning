import pygame 
import sys
from settings import Settings
from blob import Blob
from map import Map
from q_learning import Q_learning

class The_Blob:

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.total_width,
            self.settings.screen_height))
        pygame.display.set_caption("The Blob")
        self.blob = Blob(self)
        self.map = Map(self)
        self.spawn_tile = self.map.create_map_rects(return_spawn_tile=True)
        self.score = 0
        self.font_score = pygame.font.SysFont(None, 25)
        self.QL = Q_learning(self)
        
    def run_game(self):
        """"Main loop of the game."""
        while True:
            self.check_events()
            #self.update_screen()
            #self.blob.move_blob()
            self.QL.q_learning(epsilon=0.5, alpha=0.1, gamma = 0.95, episodes = 100)
            #self.detect_collision()


            # For every second, at most "self.fps" frames may pass.
            clock = pygame.time.Clock()
            clock.tick(self.settings.fps)



    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:

                #print([self.blob.rect.x // self.settings.block_size, 
                    #self.blob.rect.y // self.settings.block_size])
                # print([self.settings.map[self.blob.rect.y // self.settings.block_size, self.blob.rect.x // self.settings.block_size]])

                # To prevent diagonal movement
                self.blob.move_right = False
                self.blob.move_left = False
                self.blob.move_up = False
                self.blob.move_down = False

                if event.key == pygame.K_RIGHT:
                    self.blob.move_right = True
                if event.key == pygame.K_LEFT:
                    self.blob.move_left = True
                if event.key == pygame.K_UP:
                    self.blob.move_up = True
                if event.key == pygame.K_DOWN:
                    self.blob.move_down = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: 
                    self.blob.move_right = False
                if event.key == pygame.K_LEFT:
                     self.blob.move_left = False
                if event.key == pygame.K_UP:
                    self.blob.move_up = False
                if event.key == pygame.K_DOWN:
                    self.blob.move_down = False
            



    def update_screen(self):
        """Update images on screen and flip to new screen."""
        pygame.display.update() # update() is same as flip() as long no arguments are passed
        self.screen.fill(self.settings.bg_color)
        self.draw_grid()
        self.display_score()
        self.map.draw_map()
        self.blob.draw_blob()


    def display_score(self):
        """Display score text and score in top right corner"""
        self.text_score = self.font_score.render("Score: " + str(self.score), True, (255,255,255))
        self.screen.blit(self.text_score, self.text_score.get_rect(center = (950,150)))


    def draw_grid(self):
        """Draw background grid."""
        block_size = self.settings.block_size
        for y in range(self.settings.screen_height // block_size):
            for x in range(self.settings.screen_width // block_size):
                # Create a rect at position (y,x)*blocksize with the size of blocksize^2
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                # Draw the rectangle on screen, with color 200^3, and with bordersize of 1
                pygame.draw.rect(self.screen, (200,200,200), rect, 1)

    def detect_collision(self):
        """Detects collisions and calls proper collision function."""
        block_size = self.settings.block_size

        for tile in self.map.tiles:
            if [self.blob.rect.x // block_size, self.blob.rect.y // block_size] == [tile[1].x, tile[1].y]:
                
                # Green (goal) collision, send back to spawn, positive points.
                if tile[0] == 2:
                    self.goal_collision()

                # Red (lava) collision, send back to spawn, negative points.
                if tile[0] == 3:
                    self.lava_collision()

                # Blue (water) collision, negative points.
                if tile[0] == 4:
                    self.water_collision()


    def goal_collision(self):
        #Implement when QL is done.
        self.blob.rect.topleft = [self.settings.block_size*i for i in self.spawn_tile]
        self.score += 10
        print("Goal Collision")  


    def lava_collision(self):
        self.blob.rect.topleft = [self.settings.block_size*i for i in self.spawn_tile]
        self.score += -10

    def water_collision(self):
        #Implement when QL is done.
        self.score += -2
        print("Water Collision")  



if __name__ == "__main__":
    # Make instance of game and run game.
    blob_game = The_Blob()
    blob_game.run_game()