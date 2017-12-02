import gym
import gym_gazebo
import jaco_gym
import time
import numpy
import random
import time
import json

from tensorforce.agents import Agent
from tensorforce.execution import Runner
from tensorforce.contrib.openai_gym import OpenAIGym
from tensorforce.agents.ppo_agent import PPOAgent


network_spec = [
	dict(type='dense', size=32, activation='relu'),
	dict(type='dense', size=32, activation='relu')
]


def main():
	#tensorforce
	env = OpenAIGym('JacoArm-v0')

	agent = agent = PPOAgent(
		states_spec=env.states,
		actions_spec=env.actions,
		network_spec=network_spec,
		batch_size=1000,
		step_optimizer=dict(
			type='adam',
			learning_rate=1e-4
		)
	)

	runner = Runner(agent=agent, environment=env)

	raw_input("hit enter when gazebo is loaded...")
	runner.run(episodes=1000, max_episode_timesteps=100, episode_finished=episode_finished)

	#old-fashioned way
	# env = gym.make('JacoArm-v0')
	# print "launching the world..."
	# #gz loaing issues, let user start the learning
	# raw_input("hit enter when gazebo is loaded...")
	# env.set_physics_update(0.0001, 10000)
	# raw_input("hit enter when gazebo is loaded...")

	# # env.set_goal([0.167840578046, 0.297489331432, 0.857454500127])

	# total_episodes = 100
	# action = [1,1,1,1,1,1,1,1,1,1]
	# x = 0
	# # for x in range(total_episodes):
	# while True:
	# 	# if x % 10 is 0:
	# 	action = numpy.random.rand(1, 10)[0]
	# 		# print 'new action is', action
		
	# 	state, reward, done, _ = env.step(action)
	# 	print reward
	# 	time.sleep(0.2)
	# 	x += 1


	env.close()

def episode_finished(r):
	print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep, reward=r.episode_rewards[-1]))
	return True

if __name__ == '__main__':
	main()