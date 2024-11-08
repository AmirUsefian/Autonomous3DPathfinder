import numpy as np
import random
from environment import Environment

class Agent:
    def __init__(self, env, alpha, gamma, epsilon, episodes):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.episodes = episodes
        self.state = env.start
        self.Q = env.Q

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(range(self.env.action_space_size))  # Explore
        else:
            return np.argmax(self.Q[state[0], state[1], state[2]])  # Exploit

    def train(self):
        for episode in range(self.episodes):
            state = self.env.start
            done = False
            steps = 0
            while not done and steps < 100:
                action = self.choose_action(state)
                
                # Apply the chosen action to get the next state
                next_state = self.env.apply_action(action, state[0], state[1], state[2])
                
                # Compute the reward for the next state
                reward = self.env.compute_reward(next_state)

                # Update the Q-value based on the reward and next state's max Q-value
                old_q_value = self.Q[state[0], state[1], state[2], action]
                next_max_q_value = np.max(self.Q[next_state[0], next_state[1], next_state[2]])
                self.Q[state[0], state[1], state[2], action] = old_q_value + self.alpha * (reward + self.gamma * next_max_q_value - old_q_value)

                if state == next_state:
                    action = random.choice(range(self.env.action_space_size))  # Choose a random action to break the loop

                state = next_state
                steps += 1

    def find_optimal_path(self):
        path = [self.env.start]
        state = self.env.start
        steps = 0  # Step counter to prevent infinite loops

        while state != self.env.goal and steps < 100:
            action = np.argmax(self.Q[state[0], state[1], state[2]])  # Choose best action
            next_state = self.env.apply_action(action, state[0], state[1], state[2])
            path.append(next_state)
            state = next_state
            steps += 1

        return path



