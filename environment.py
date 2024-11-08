import random
import numpy as np

class Environment:
    def __init__(self, grid_size, num_layers, goal, start, obstacles):
        self.grid_size = grid_size
        self.num_layers = num_layers
        self.goal = goal
        self.start = start
        self.obstacles = obstacles
        self.action_space_size = 6
        self.Q = np.zeros((num_layers, grid_size, grid_size, self.action_space_size))
    
    def apply_action(self, action, layer, x, y):
        if action == 0:
            return (layer, max(0, x - 1), y)  # Up
        elif action == 1:
            return (layer, min(self.grid_size - 1, x + 1), y)  # Down
        elif action == 2:
            return (layer, x, max(0, y - 1))  # Left
        elif action == 3:
            return (layer, x, min(self.grid_size - 1, y + 1))  # Right
        elif action == 4:
            return (min(self.num_layers - 1, layer + 1), x, y)  # Up-layer
        elif action == 5:
            return (max(0, layer - 1), x, y)  # Down-layer

    def compute_reward(self, next_state):
        if next_state in self.obstacles:
            return -10  
        elif next_state == self.goal:
            return 10  
        else:
            return -0.5  

def move_obstacles(obstacles, grid_size, num_layers):
    new_obstacles = []
    for (layer, x, y) in obstacles:
        action = random.choice([0, 1, 2, 3, 4, 5])
        new_pos = apply_obstacle_action(action, layer, x, y, grid_size, num_layers)
        new_obstacles.append(new_pos)
    return new_obstacles

def apply_obstacle_action(action, layer, x, y, grid_size, num_layers):
    if action == 0:
        return (layer, max(0, x - 1), y)
    elif action == 1:
        return (layer, min(grid_size - 1, x + 1), y)
    elif action == 2:
        return (layer, x, max(0, y - 1))
    elif action == 3:
        return (layer, x, min(grid_size - 1, y + 1))
    elif action == 4:
        return (min(num_layers - 1, layer + 1), x, y)
    elif action == 5:
        return (max(0, layer - 1), x, y)

