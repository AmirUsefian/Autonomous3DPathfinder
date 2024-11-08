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
            return random.choice(range(self.env.action_space_size)) 
        else:
            return np.argmax(self.Q[state[0], state[1], state[2]])  

    def train(self):
        for episode in range(self.episodes):
            state = self.env.start
            done = False
            steps = 0
            while not done and steps < 100:
                action = self.choose_action(state)
                
                next_state = self.env.apply_action(action, state[0], state[1], state[2])
                
                reward = self.env.compute_reward(next_state)

                old_q_value = self.Q[state[0], state[1], state[2], action]
                next_max_q_value = np.max(self.Q[next_state[0], next_state[1], next_state[2]])
                self.Q[state[0], state[1], state[2], action] = old_q_value + self.alpha * (reward + self.gamma * next_max_q_value - old_q_value)

                if state == next_state:
                    action = random.choice(range(self.env.action_space_size))  

                state = next_state
                steps += 1

    def find_optimal_path(self):
        path = [self.env.start]
        state = self.env.start
        steps = 0 

        while state != self.env.goal and steps < 100:
            action = np.argmax(self.Q[state[0], state[1], state[2]])  
            next_state = self.env.apply_action(action, state[0], state[1], state[2])
            path.append(next_state)
            state = next_state
            steps += 1

        return path



