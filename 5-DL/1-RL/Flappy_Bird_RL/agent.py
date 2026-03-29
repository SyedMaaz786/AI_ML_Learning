import torch
import torch.optim as optim
import numpy as np
from dqn import DQN
from experience_replay import ReplayBuffer


class Agent:
    def __init__(self, state_dim, action_dim):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.q_net = DQN(state_dim, action_dim).to(self.device)
        self.target_net = DQN(state_dim, action_dim).to(self.device)
        self.target_net.load_state_dict(self.q_net.state_dict())

        self.optimizer = optim.Adam(self.q_net.parameters(), lr=1e-3)
        self.buffer = ReplayBuffer(10000)

        self.gamma = 0.99
        self.batch_size = 64
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(2)

        state = np.array(state).flatten()
        state = torch.FloatTensor(state).unsqueeze(0).to(self.device)

        q_values = self.q_net(state)
        return torch.argmax(q_values).item()

    def train(self):
        if len(self.buffer) < self.batch_size:
            return

        states, actions, rewards, next_states, dones = self.buffer.sample(self.batch_size)

        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)

        q_values = self.q_net(states).gather(1, actions.unsqueeze(1)).squeeze()

        next_q = self.target_net(next_states).max(1)[0]
        target = rewards + self.gamma * next_q * (1 - dones)

        loss = torch.nn.functional.mse_loss(q_values, target.detach())

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def update_target(self):
        self.target_net.load_state_dict(self.q_net.state_dict())


if __name__ == "__main__":
    import yaml
    from flappy_bird import FlappyBirdEnv

    LOAD_MODEL = True  


    with open("parameters.yaml", "r") as f:
        params = yaml.safe_load(f)

    env = FlappyBirdEnv(render=False)
    state = np.array(env.reset()).flatten()

    state_dim = len(state)
    agent = Agent(state_dim=state_dim, action_dim=2)

    episodes = params["episodes"]


    if LOAD_MODEL:
        agent.q_net.load_state_dict(torch.load("model.pth"))
        agent.q_net.eval()
        print("Model Loaded!")

    else:
        best_reward = -float("inf")


        for episode in range(episodes):
            state = np.array(env.reset()).flatten()
            total_reward = 0

            while True:
                action = agent.select_action(state)
                next_state, reward, done = env.step(action)

                agent.buffer.push(state, action, reward, next_state, done)
                agent.train()

                state = np.array(next_state).flatten()
                total_reward += reward

                if done:
                    break


            if total_reward > best_reward:
                best_reward = total_reward
                torch.save(agent.q_net.state_dict(), "model.pth")
                print(f"New Best Model Saved! Reward: {best_reward}")

            if episode % params["target_update"] == 0:
                agent.update_target()

            if episode % 100 == 0:
                print(f"Episode {episode}, Reward: {total_reward}")

        print("Training Completed!")


    env = FlappyBirdEnv(render=True)

    agent.epsilon = 0.0
    state = env.reset()

    while True:
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)

        state = next_state

        if done:
            state = env.reset()