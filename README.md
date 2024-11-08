# Autonomous Pathfinding in 3D Environments using Q-Learning

This project demonstrates the use of reinforcement learning, specifically Q-learning, to train an autonomous agent to navigate a 3D maze environment. The agent learns to avoid dynamic obstacles and efficiently find the shortest path to a predefined goal. The agent's learning process is visualized in 3D, showcasing its pathfinding abilities and its interactions with the environment.

## Project Overview

The project is designed to simulate a real-world application of reinforcement learning in a dynamic 3D environment. The key components of the system include:
- **3D Grid Environment**: A virtual maze with dynamic obstacles and a goal state.
- **Q-Learning Agent**: An autonomous agent that uses Q-learning to explore the environment and learn the optimal path.
- **Dynamic Obstacles**: Obstacles move periodically within the environment, challenging the agent to adapt its strategy.
- **Visualization**: After training, the optimal path taken by the agent is visualized in 3D, alongside obstacles and the goal.

### Key Features:
- **3D Grid Navigation**: The agent operates in a 3D grid with multiple layers, simulating a more complex environment than traditional 2D grids.
- **Dynamic Obstacles**: Obstacles move every few steps, creating an environment where the agent needs to react in real-time.
- **Reinforcement Learning**: The agent utilizes Q-learning, a model-free reinforcement learning algorithm, to update its knowledge base and improve its decision-making process.
- **Exploration vs. Exploitation**: The agent balances between exploring new actions and exploiting its learned knowledge using an epsilon-greedy strategy.
- **Pathfinding Algorithm**: After training, the agent can find the optimal path to the goal, avoiding obstacles and maximizing rewards.

## Installation

To get started with this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/3d-maze-pathfinding.git
cd 3d-maze-pathfinding
pip install -r requirements.txt
