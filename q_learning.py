import numpy as np


class Q_learning:

    def __init__(self, blob_game):

        self.settings = blob_game.settings
        self.map = self.settings.map
        self.blob = blob_game.blob
        self.blob_game = blob_game
        self.q_map = np.zeros((16,16,4))

        #self.Q_map = np.zeros((x_size, y_size, 4))

        # epsilon = 0.5
        # alpha = 0.1
        # gamma = 0.95
        # episodes = 100

    def q_learning(self, epsilon, alpha, gamma, episodes):
        bs = self.settings.block_size

        for episode in range(episodes):
            
            # Start each episode at spawn
            s = self.blob_game.spawn_tile

            while True:
                current_actions = self.q_map[s[0],[1],:]
                q = int(np.max(current_actions))
                
                # Action
                a = np.random.choice(np.where(np.array(current_actions == q))[1])

                #[right,left,up,down]
                if a == 0:
                    self.blob.move_right == True
                elif a == 1:
                    self.blob.move_left == True
                elif a == 2:
                    self.blob.move_up == True
                elif a == 3:
                    self.blob.move_down == True
                self.blob.move_blob()
                self.blob_game.detect_collision()
                self.blob_game.update_screen()

                # New state
                new_s = [self.blob.rect.x // bs ,self.blob.rect.y // bs]

                # Reward
                r = self.map[new_s[0],new_s[1]] 
                

                ### FORTSÄTT HÄR
                # Max_a Q(S',a)
                future_max_q = np.max(self.Q_map[new_s[0],new_s[1]]) 

                # New q_value 
                new_q = q + alpha*(r + gamma*future_max_q - q)

                # Update Q policy map.
                self.q_map[s[0],s[1],a] = new_q

                # Update old state to new state
                s = new_s

                # Check if we hit terminal state
                if r == 10 or r == -10:
                    break




