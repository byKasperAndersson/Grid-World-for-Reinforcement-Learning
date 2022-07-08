import numpy as np

# To test the game yourself, let manual = True. To use Q-learning, let manual = False.
manual = False

# Design your own map. Four pre done maps are included, see below.
# Make sure to change variable map_to_play to the map you want to load the game with, see below.

# Tiles available tiles of map. Every map should have atleast one spawn tile 
# 0 = Standard (no) tile. This has no affect. 
# 1 = White (spawn) tile. The blob spawns here. There should only be one spawn tile.
# 2 = Green (goal) tile. You get +1 points. Episode ends when goal is reached.
# 3 = Red (lava) tile. You get -1 points. Episode ends when lava is reached.
# 4 = Blue (water) tile. This gives it -0.2 points.

#5x8 map with only spawn and goal.
map1 = np.array([[0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,2,0],
                 [0,0,0,0,0,0,0,0]])

#5x8 map with 1 lava tile, spawn and goal
map2 = np.array([[0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,3,0,0,0,0],
                 [0,0,0,0,0,0,2,0],
                 [0,0,0,0,0,0,0,0]])

#10x10 map with spawn, goal and some lava.
map3 = np.array([[0,0,0,0,0,0,0,0,0,0],
                 [0,1,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,2,0],
                 [0,0,0,0,0,0,0,0,0,0]])


#10x10 map with spawn,goal and more lava.
map3 = np.array([[0,0,0,0,0,3,0,0,0,0,0],
                 [0,1,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,0,3,0,0,0,0,0],
                 [3,3,0,3,3,3,3,3,0,3,3],
                 [0,0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,0,3,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,3,0,0,0,2,0],
                 [0,0,0,0,0,3,0,0,0,0,0]])

#8x18 map with spawn, goal, lava and water. (hard)
map4 = np.array([[0,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,3,4],
                 [0,0,3,3,3,0,3,0,3,0,3,0,3,0,3,0,3,4],
                 [0,0,3,0,3,0,3,0,3,0,3,0,3,0,3,0,3,4],
                 [0,0,3,0,3,0,3,0,3,0,3,0,3,0,3,0,3,4],
                 [0,0,3,0,3,0,0,0,3,0,0,0,0,0,3,0,0,4],
                 [0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4],
                 [1,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4],
                 [0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]])


# Map to be loaded into Grid World.
map_to_play = map4

# Episodes to be played before game over. Relevant variable in reinforcement learning.
episodes = 50 

# Settings for Q-Learning. Can be ignored if playing manually.
epsilon = 0.2
alpha = 0.2
gamma = 0.9