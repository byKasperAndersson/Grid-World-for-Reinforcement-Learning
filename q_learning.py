from tkinter import S
import numpy as np


class Q_learning:

    def __init__(self, blob_game):

        self.settings = blob_game.settings
        self.map = self.settings.map
        self.blob = blob_game.blob
        self.blob_game = blob_game
        self.q_map = np.zeros((10,10,4))

        #self.Q_map = np.zeros((x_size, y_size, 4))

        # epsilon = 0.5
        # alpha = 0.1
        # gamma = 0.95
        # episodes = 100

    def q_learning(self, epsilon, alpha, gamma, episodes):
        bs = self.settings.block_size
        ii = 0

        for episode in range(episodes):
            
            # Start each episode at spawn
            s = self.blob_game.spawn_tile

            while True:
                ii += 1

                # np.array of rewards for taking each action at current state (tile). 
                # format is [right,left,up,down].
                current_actions =  self.q_map[s[0],s[1],:]

                # Max value a current state
                q = np.max(current_actions)
                
                print(current_actions)

                # Action (epsilon greedy)
                # With probability 1-epsilon, choose most rewarding action.
                # With probability epsilon, choose random action.
                a_choice = np.random.choice(["best", "random"], p = [1-epsilon, epsilon])
                if a_choice == "best":
                    a = np.random.choice(np.where(np.array(current_actions == q))[1])
                if a_choice == "random":
                    a = np.random.choice([0,1,2,3])

                print(a)
                #[right,left,up,down]
                if a == 0:
                    self.blob.move_right = True
                    #print(a)
                elif a == 1:
                    self.blob.move_left = True
                    #print(a)
                elif a == 2:
                    self.blob.move_up = True
                    #print(a)
                elif a == 3:
                    self.blob.move_down = True
                    #print(a)
                
                    
                self.blob.move_blob()
                self.blob_game.detect_collision()
                self.blob_game.update_screen()

                # New state
                new_s = [self.blob.rect.x // bs ,self.blob.rect.y // bs]

                # Reward
                r = self.map[new_s[0],new_s[1]] 
                
                # Max_a Q(S',a)
                future_max_q = np.max(self.q_map[new_s[0],new_s[1]]) 

                # New q_value 
                new_q = q + alpha*(r + gamma*future_max_q - q)

                # Update Q policy map.
                self.q_map[s[0],s[1],a] = new_q

                # Update old state to new state
                s = new_s

                # Check if we hit terminal state
                if r == 10 or r == -10:
                    print("Now we break")
                    break




