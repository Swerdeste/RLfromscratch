import torch
import random
import numpy as np
from collections import deque
from test import Game
from idk import *
from helper import plot
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.03

class Agent() :
    def __init__(self) :
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(10, 10, 4)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        
    
    
    def get_state(self,game) :
        mat = game.get_grill()
        return mat

    def get_action(self,state,game) :
        self.epsilon = 80 - self.n_games
        nb_col = game.get_nb_col()
        final_move = [0 for i in range(nb_col)] 
        if random.randint(0, 200) > self.epsilon:
            move = random.randint(0, nb_col -1)
            final_move[move] = 1
        #else : 
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            print("-------",state0,"-------",prediction)
            print("++*fdfdd", move,"fdfdfd", final_move)
            final_move[move] = 1
        return final_move
        

    def remember(self,state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))


    def train_long_memory(self) :
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done) :
        self.trainer.train_step(state, action, reward, next_state, done)


#################################### 

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    agent = Agent()
    game = Game(10,3)
    i = 0
    record = game.get_max_move()
    counter = 0
    while True:
        # get old state
        print(game.get_grill())
        print("     --------       ")



        state_old = agent.get_state(game)
        print(state_old)
        print("     --------       ")
        # get move
        final_move = agent.get_action(state_old,game)
        print(final_move)
        print("     --------       ")

        print("     --------       ")

        # perform move and get new state


        reward, counter, endgame = game.Tour(final_move, old_val = state_old[0][0], counter = counter)
        state_new = agent.get_state(game)

        # train short memory

        agent.train_short_memory(state_old, final_move, reward, state_new, endgame)

        # remember
        agent.remember(state_old, final_move, reward, state_new, endgame)
        print(counter)
        print("+++++++++++++++")
        if endgame == True:
            # train long memory, plot result
        
            agent.n_games += 1
            agent.train_long_memory()

            if counter < record:
                record = counter
                agent.model.save()

            print('Game', agent.n_games, 'Score', counter, 'Record:', record)

            plot_scores.append(record)
            total_score += counter
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
            game.reset()
            counter=0

        print(i)
        i+=1

if __name__ == '__main__':
    train()
