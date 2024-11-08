# Autonomous3DPathfinder

**Autonomous3DPathfinder** is a reinforcement learning-based agent designed to navigate a 3D Grid environment and find the optimal path from a start position to a goal while avoiding dynamic obstacles. The agent uses Q-learning to improve its decision-making over multiple episodes. It incorporates real-world challenges, such as moving obstacles, to mimic realistic pathfinding problems.

### Features

- **3D Grid Navigation:** The agent can navigate a 3D grid (layers, rows, columns) to find the shortest path to the goal.
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
6. [Contributing](#contributing)

---

## Installation

To get started with **Autonomous3DPathfinder**, you need to clone the repository and install the required dependencies. You can do so by following the steps below.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Autonomous3DPathfinder.git
   cd Autonomous3DPathfinder
   ```

2.Install the necessary dependencies
   ```bash
   pip install -r requirements.txt
   ```

---

## dependencies
 
Autonomous3DPathfinder requires the following Python packages:

    numpy
    matplotlib
    random

Install all dependencies using the provided requirements.txt

---

## usage

Once the dependencies are installed, you can run the program and train the agent to navigate through the 3D maze

1.Run the agent and start training:
   ```bash
     python main.py
   ```

2.After training, the agent will find the optimal path, and the results will be displayed in a 3D plot, showing the path taken by the agent and the locations of dynamic obstacles.

---

## training-the-agent

Training the agent involves running the Q-learning algorithm for a specified number of episodes. During training, the agent will:

   1.Start from the initial state.

   2.Take actions based on the epsilon-greedy policy.

   3.Receive rewards based on its interactions with the environment.

   4.Update its Q-table after each action.

The agent will continue training for a set number of episodes or until it reaches the goal.

---

## visualizing-the-path

After the agent completes training, the optimal path is visualized using matplotlib in a 3D plot, which helps you understand how the agent navigated through the grids while avoiding obstacles.

---

## contributing

I welcome contributions to Autonomous3DPathfinder! If you would like to contribute:

   1.Fork the repository.

   2.Create a new branch.

   3.Make your changes.

   4.Submit a pull request.

Please ensure that your code follows the PEP8 style guide and includes relevant test cases.
