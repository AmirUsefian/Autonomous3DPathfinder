# Autonomous3DPathfinder

**Autonomous3DPathfinder** is a reinforcement learning-based agent designed to navigate a 3D maze environment and find the optimal path from a start position to a goal while avoiding dynamic obstacles. The agent uses Q-learning to improve its decision-making over multiple episodes. It incorporates real-world challenges, such as moving obstacles, to mimic realistic pathfinding problems.

### Features

- **3D Maze Navigation:** The agent can navigate a 3D grid (layers, rows, columns) to find the shortest path to the goal.
- **Dynamic Obstacles:** Obstacles in the environment move randomly at set intervals, adding complexity to the pathfinding challenge.
- **Q-Learning:** The agent uses Q-learning to update its action-value function and improve its performance over time.
- **Epsilon-Greedy Policy:** The agent explores the environment randomly with a probability (epsilon) to ensure effective exploration and exploitation.
- **Optimal Path Finding:** After training, the agent can find the best path from start to goal based on its learned Q-table.

---

## Table of Contents

1. [Installation](#installation)
2. [Dependencies](#dependencies)
3. [Usage](#usage)
4. [Training the Agent](#training-the-agent)
5. [Visualizing the Path](#visualizing-the-path)
6. [Directory Structure](#directory-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

To get started with **Autonomous3DPathfinder**, you need to clone the repository and install the required dependencies. You can do so by following the steps below.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Autonomous3DPathfinder.git
   cd Autonomous3DPathfinder

---

2.Install the necessary dependencies
   ```bash
   pip install -r requirements.txt
