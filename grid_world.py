import pygame 
import sys
from settings import Settings
from agent import Agent
from map import Map
import numpy as np

class Grid_World:

    def __init__(self):
        """Initialize the game and ."""
        pygame.init()

        # General settings for the game
        self.settings = Settings()

        # Game Initialize, loaded from settings.py. Adjustable in player_settings.py.
        self.score = self.settings.score
        self.episodes = self.settings.episodes
        self.current_episode = self.settings.current_episode 

        # Reinforcement learnining settings, loaded from settings.py. Adjustable in player_settings.py.
        self.q_table = self.settings.q_table
        self.epsilon = self.settings.epsilon
        self.alpha = self.settings.alpha
        self.gamma = self.settings.gamma

        # Game fonts
        self.screen = pygame.display.set_mode((self.settings.total_width,
            self.settings.screen_height))
        pygame.display.set_caption("Grid World")
        self.font_score = pygame.font.SysFont(None, 25)
        self.font_q_table = pygame.font.SysFont(None,15)

        # More game settings
        self.map = Map(self)
        # Create map, returns spawn_tile. Needed for some functions.
        self.spawn_tile = self.map.create_map_rects(return_spawn_tile=True)
        self.agent= Agent(self)

        # Create map, returns spawn_tile. Needed for some functions.
        self.spawn_tile = self.map.create_map_rects(return_spawn_tile=True)

    def run_game(self):
        """"Main loop of the game."""

        while True:
            if self.settings.manual:    
                self.check_events(self.settings.manual)
                self.update_screen()
                self.agent.move_agent(self.settings.manual)
                #self.detect_collision()
            else:
                self.q_learning(self.spawn_tile, self.epsilon, self.alpha, self.gamma)

            # For every second, at most "self.fps" frames may pass.
            clock = pygame.time.Clock()
            clock.tick(self.settings.fps)

        # while self.current_episode > self.episodes:
        #     self.check_events(self.settings.manual)
        #     self.display_q_table()

    def check_events(self,manual):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            print(self.score)
            if event.type == pygame.QUIT:
                sys.exit()
            
            if manual: 
                if event.type == pygame.KEYDOWN:

                    # To prevent diagonal movement
                    self.agent.move_right = False
                    self.agent.move_left = False
                    self.agent.move_up = False
                    self.agent.move_down = False

                    if event.key == pygame.K_RIGHT:
                        self.agent.move_right = True
                    if event.key == pygame.K_LEFT:
                        self.agent.move_left = True
                    if event.key == pygame.K_UP:
                        self.agent.move_up = True
                    if event.key == pygame.K_DOWN:
                        self.agent.move_down = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT: 
                        self.agent.move_right = False
                    if event.key == pygame.K_LEFT:
                        self.agent.move_left = False
                    if event.key == pygame.K_UP:
                        self.agent.move_up = False
                    if event.key == pygame.K_DOWN:
                        self.agent.move_down = False
                



    def update_screen(self):
        """Update images on screen and flip to new screen."""
        pygame.display.update() # update() is same as flip() as long no arguments are passed
        self.screen.fill(self.settings.bg_color)
        self.draw_grid()
        self.display_score()
        self.map.draw_map()
        self.agent.draw_agent()
        if self.current_episode > self.episodes:
            self.display_q_table()
            

    def display_score(self):
        """Display score and episode in top right corner"""
       
        # Score
        self.text_score = self.font_score.render("Score: " + str(self.score), True, (255,255,255))
        x_center = self.settings.screen_width + (self.settings.screen_score_width // 2)
        self.screen.blit(self.text_score, self.text_score.get_rect(center = (x_center,100)))

        # Episode
        self.text_episode = self.font_score.render("Episodes : " + str(self.current_episode) + "/" + str(self.episodes), True, (255,255,255))
        x_center = self.settings.screen_width + (self.settings.screen_score_width // 2)
        self.screen.blit(self.text_episode, self.text_episode.get_rect(center = (x_center,150)))


    def draw_grid(self):
        """Draw background grid."""
        block_size = self.settings.block_size
        for y in range(self.settings.screen_height // block_size):
            for x in range(self.settings.screen_width // block_size):
                # Create a rect at position (y,x)*blocksize with the size of blocksize^2
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                # Draw the rectangle on screen, with color 200^3, and with bordersize of 1
                pygame.draw.rect(self.screen, (200,200,200), rect, 1)


    ### Q_learning

    """Recall that (x,y) in cartesian coordinates is (x,-y) on screen. Also,
        np.arrays are called as (row, column), so (x,y) in cartesian coordinate
        is row = x and column = y. So to return cartesian 
        position (x,y) in 2d np.array, call np.array[y,x]. """

    def greedy_policy(self,x,y):
        """Returns highest rewarding action from q_table at position (x,y)."""

        # np.array of rewards for taking each action at current state (tile). 
        # format is [right,up,left,down], keep this for easier display score.
        current_actions = self.q_table[y,x,:]

        # Max value at current state
        q = np.max(current_actions)

        # Most valued action to do, that is, where to go.
        action = np.random.choice(np.where(np.array(current_actions == q))[0])

        return action

    
    def epsilon_greedy_policy(self, x, y, epsilon):
        """Returns highest rewarding action from q_table at position (x,y) with probability 
            1-epsilon and a random action with probability epsilon."""

        action_choice = np.random.choice(["best", "random"], p = [1-epsilon, epsilon])
        if action_choice == "best":
            action = self.greedy_policy(x,y)
        if action_choice == "random":
            action = np.random.choice([0,1,2,3])

        return action


    def transition(self, x, y, action):
        """"Returns new state after performing action at position (x,y)."""

        #[right,up,left,down], keep this format for easier display score.
        delta = [[1,0], [0,-1], [-1,0], [0,1]][action]

        # Move current state with delta. If new state is outside map, return old state.
        # np.array ???
        new_state = [x+delta[0], y+delta[1]]
        if (new_state[0] < 0) or (new_state[0] > (self.settings.map.shape[1] - 1)) or \
            (new_state[1] < 0) or (new_state[1] > (self.settings.map.shape[0] - 1)):
            new_state = [x,y]

        return new_state

    
    def q_learning(self, start_state, epsilon, alpha, gamma):

        state = start_state
        cumulative_change  = 0
        reward = 0

        while True:
            
            if self.current_episode <= self.episodes:
                
                # Current position. (State not np.array, so format is OK.)
                x = state[0]
                y = state[1]
    
                ### Calculate relevant information for updating Q-table and to move agent.

                # Choose an action
                action = self.epsilon_greedy_policy(x,y,epsilon)
                # Get new state
                new_state = self.transition(x,y,action)
                # Reward at new state (new_state not np.array, so format is OK.)
                reward_index = self.settings.map[new_state[1],new_state[0]]
                reward = self.settings.rewards[reward_index]
                

                ### Update Q-table

                # Update cumulative sum of episode adjustments
                cumulative_change += reward + gamma*np.max(self.q_table[new_state[1],new_state[0]]) -\
                    self.q_table[y,x,action]

                # Correction of current episode
                change = alpha*(reward + gamma*np.max(self.q_table[new_state[1],new_state[0]]) - self.q_table[y,x,action])

                # Update q_table (global variable), i.e,
                # Q(S,A) := Q(S,A) + alpha*( R + gamma*max_aQ(S',a) - Q(S,A) ) 
                self.q_table[y,x,action] += change
                
                # Update game
                self.update_screen()
                self.agent.move_agent(self.settings.manual, algorithm_movement = new_state)
                #self.detect_collision()

                # Update state
                state = new_state
                # If we hit terminal state (lava or goal), end episode
                if reward == -10 or reward == 10:
                    #print("Reward: " + str(reward))
                    return([reward, cumulative_change])

            else:
                self.check_events(self.settings.manual)
                self.update_screen()
                #print(self.q_table)


            

    def display_q_table(self):         
        for y in range(self.settings.screen_height // self.settings.block_size):
            for x in range(self.settings.screen_width // self.settings.block_size):
                if self.settings.map[y,x] not in [2,3]:
                    for action in [0,1,2,3]:
                        xx = 20*np.cos(action*np.pi/2)
                        yy = 25*np.sin(action*np.pi/2)
                        #self.text_qvalue1 = self.font_q_table.render( \
                            #str((x,y)), action, True, (255,255,255))
                            
                        self.text_qvalue = self.font_q_table.render( \
                            str(round(self.q_table[y,x,action],4)), action, True, (255,255,255))

                        self.screen.blit(self.text_qvalue, self.text_qvalue.get_rect(center = \
                            ((x+1/2)*self.settings.block_size + xx, (y+1/2)*self.settings.block_size - yy)))

                        # Displays position, for testing
                        #self.screen.blit(self.text_qvalue1, self.text_qvalue1.get_rect(center = \
                            #((x+1/2)*self.settings.block_size, (y+1/2)*self.settings.block_size)))



#str(round(self.q_table[x,y,0]))



if __name__ == "__main__":
    # Make instance of game and run game.
    grid_world = Grid_World()
    grid_world.run_game()