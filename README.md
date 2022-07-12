# Grid World for Reinforcement Learning

Grid World is a simple game where you control an agent on a grid map. The goal is to take the agent from spawn to goal without touching the lava and to avoid the water as much as possible. Furthermore, Q-Learning, which is a machine learning algorithm of the type reinforcement learning, is implemented and it can be used to train the agent to find its own path on the grid. A simple text file map editor is included which allows the player to design their own challanges for the Q-Learning agent to beat.  

![Map1](Images/map1.PNG)
![Map3](Images/map3.PNG)
![Map_q_table](Images/mapqtable.PNG)

## Change game settings
Adjustable game settings, such as Q-Learning variables, maps, episodes to be played etc. can be edited in file `player_settings.py`.

## The Game

The agent is of yellow colour and is controlled with arrow keys if `manual = True` or by the Q-Learning algorithm if `manual = False`.

The maps consist of six different tiles.
- Standard (black) tile. These tiles has no specific effect on the game.
- Spawn (white) tile. The agent spawns here each episode.
- Goal (green) tile. Rewards +10 points and episode ends.
- Lava (red) tile. Rewards -10 points and episode ends.
- Water (blue) tile. Rewards -1 points and episode continues. 

The game continues until all episodes are finished, and if Q-Learning is used a Q-Table will be displayed in the end.


## The Q-Learning algorithm

To be written.


## To-Do List
- Show which Q-Learning variables are used during play
- Implement other reinforcement learning algorithms, such as Deep Reinforcement Learning.
- Implement decaying rates for the Q-Learning. 

