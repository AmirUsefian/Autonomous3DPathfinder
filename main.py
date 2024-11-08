from environment import Environment
from agent import Agent
from utils import move_obstacles
from visualization import plot_path_and_obstacles

def main():
    # Initialize environment, agent, and parameters
    env = Environment(grid_size=5, num_layers=3, goal=(2, 4, 4), start=(0, 0, 0), obstacles=[(0, 1, 1), (1, 2, 1), (2, 3, 3), (2, 3, 2)])
    agent = Agent(env=env, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=1000)

    # Train agent using Q-learning
    agent.train()

    # Find the optimal path after training
    optimal_path = agent.find_optimal_path()

    # Visualize the path and obstacles
    plot_path_and_obstacles(optimal_path, env.obstacles, env.goal)

if __name__ == "__main__":
    main()

