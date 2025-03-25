import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AppleGameEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.observation_space = spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        self.action_space = spaces.Discrete(3)

        self.state = np.array([0], dtype=np.float32)


    def step(self, action):
        pass


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        return self.state, {}


    def render(self):
        pass


    def close(self):
        pass
