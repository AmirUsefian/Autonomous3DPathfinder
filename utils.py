import random

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

