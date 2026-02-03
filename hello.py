import gymnasium as gym
from stable_baselines3 import A2C

def random_agent():   
    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset()
    print(f"Starting observation: {observation}")

    episode_over = False
    total_reward = 0

    while not episode_over:
        
        action = env.action_space.sample()  

        observation, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        episode_over = terminated or truncated

    print(f"Episode finished! Total reward: {total_reward}")
    env.close()
def train():
    env = gym.make("CartPole-v1", render_mode=None)

    model = A2C("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=100_000)
    model.save('CartPole_A2C')

def test():
    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset()
    model=A2C.load('CartPole_A2C')
    episode_over = False
    total_reward = 0

    while not episode_over:
        action,_states=model.predict(observation,deterministic=True)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        episode_over = terminated or truncated
        
    print(f"Episode finished! Total reward: {total_reward}")
    env.close()
#train()
test()