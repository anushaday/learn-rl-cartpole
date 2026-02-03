# learn-rl-cartpole
Exploring Deep RL: Training my first agent using Stable-Baselines3 and Gymnasium. Logged progress from 18 to 137+ avg reward.

Reinforcement Learning Lab: CartPole-v1 

This repository documents my first steps into Reinforcement Learning (RL). I successfully built and trained an agent to solve the **CartPole-v1** environment using the Stable-Baselines3 library!

## Project Overview
The goal of this project was to train a "brain" (agent) to balance a pole on a cart by moving it left or right. 

### Technical Details
* **Algorithm:** A2C (Asynchronous Advantage Actor Critic)
* **Policy:** MlpPolicy (Multi-Layer Perceptron)
* **Library:** Gymnasium (formerly OpenAI Gym)
* **Framework:** Stable-Baselines3 (PyTorch-based)

## Key Observations & Results
Through training, the agent learned to maximize its reward by keeping the pole upright for longer periods.

| Metric | Before Training | After Training (10k steps) |
| :--- | :--- | :--- |
| **Avg. Reward** | ~18.0 | **137.0** |
| **Status** | Unstable | Stable and Improving |

### What I Learned:
* **The RL Loop:** How the agent interacts with the environment through States, Actions, and Rewards.
* **Environment Setup:** Managing Python virtual environments and dependencies via Anaconda and VS Code.
* **Observation Space:** Tracking 4 variables (Position, Velocity, Angle, Angular Velocity) to inform the agent's decisions.
* **Reward System:** The agent receives +1 for every frame the pole stays upright, incentivizing survival.

##  How to Run
1. Create a virtual environment: `conda create -n rl_env python=3.10`
2. Install dependencies: `pip install gymnasium[classic_control] stable-baselines3`
3. Run the training script: `python hello.py`

*This project is part of my journey to master Deep Reinforcement Learning. Next up: Lunar Lander!*
