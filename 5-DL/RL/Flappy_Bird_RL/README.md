# Flappy Bird RL (DQN)

This project implements a Deep Q-Network (DQN) agent to play Flappy Bird using reinforcement learning.

## Features
- DQN (Deep Q Network)
- Experience Replay
- Target Network
- Gym-based Flappy Bird environment

## How to Run

```bash
pip install -r requirements.txt
python agent.py

## Notes

- Set `LOAD_MODEL = False` to train the agent  
- Set `LOAD_MODEL = True` to play using the trained model

Trained model (`.pth`) is not included due to size limits.
You can train the model using the provided code.