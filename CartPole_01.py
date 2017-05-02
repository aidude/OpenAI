# CartPole challenge

import numpy
import torch
import gym
import matplotlib







env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

