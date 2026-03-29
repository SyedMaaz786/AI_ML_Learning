import gymnasium as gym
import flappy_bird_gymnasium

class FlappyBirdEnv:
    def __init__(self, render=False):
        if render:
            self.env = gym.make("FlappyBird-v0", render_mode="human")
        else:
            self.env = gym.make("FlappyBird-v0")

    def reset(self):
        state, _ = self.env.reset()
        return state

    def step(self, action):
        state, reward, done, truncated, _ = self.env.step(action)
        return state, reward, (done or truncated)