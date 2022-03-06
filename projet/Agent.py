import torch
import random
import numpy as np
from collections import deque
from Game import Game
from Learning import *
from helper import plot
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.1

class Agent() :

    def __init__(self,size) :
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(size**2,128,3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        
    
    
    def get_state(self,game) :
        mat = game.get_grill()
        return mat

    def get_action(self,state,game) :
        self.epsilon = 80 - self.n_games
        nb_col = game.get_nb_col()
        final_move = [0 for i in range(nb_col)] 
        """if random.randint(0, 500) <=self.epsilon:
            move = random.randint(0, nb_col -1)
            final_move[move] = 1
        else :"""

        state0 = torch.tensor(state.ravel(), dtype=torch.float)
        prediction = self.model(state0)
        #print(prediction)
        moves = torch.argmax(prediction)
        #print(moves)
        move = moves.item() % game.get_nb_col()
        #print("-------",state0,"-------",prediction)
        #print("++*fdfdd", move,"fdfdfd", final_move)
        if move == state[0][0]: 
                new_moves = torch.topk(prediction,k=3)
                new_move = new_moves[1][2].item()% game.get_nb_col()
                
                final_move[new_move] = 1
                #print(final_move)

        else : 
            final_move[move] = 1

        #final_move[move%game.get_nb_col()] = 1
        return final_move
        

    def remember(self,state, action, reward, next_state, done):
        
        """_summary_

        Args:
            state (_type_): _description_
            action (_type_): _description_
            reward (_type_): _description_
            next_state (_type_): _description_
            done (function): _description_
        """
        self.memory.append((state.ravel(), action, reward, next_state.ravel(), done))



    def train_long_memory(self) :
        """Train long memory
        """
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done) :
        """Train short memory

        Args:
            state (_type_): _description_
            action (_type_): _description_
            reward (_type_): _description_
            next_state (_type_): _description_
            done (function): _description_
        """
        self.trainer.train_step(state.ravel(), action, reward, next_state.ravel(), done)


#################################### 

def train():
    """Train function
    """
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    agent = Agent(10)
    game = Game(10,3)
    i = 0
    record = game.get_max_move()
    counter = 0
    nwin = 0 
    while True:
        # get old state
        #print(game.get_grill())
        #print("     --------       ")



        state_old = agent.get_state(game)
        #print(state_old)
        #print("     --------       ")
        # get move
        final_move = agent.get_action(state_old,game)
        #print("     --------       ")

        #print("     --------       ")

        # perform move and get new state


        reward, counter, endgame = game.Tour(final_move, old_val = state_old[0][0], counter = counter)
        state_new = agent.get_state(game)

        # train short memory

        agent.train_short_memory(state_old, final_move, reward, state_new, endgame)

        # remember
        agent.remember(state_old, final_move, reward, state_new, endgame)
        #print(counter)
        #print("+++++++++++++++")
        if endgame == True:
            # train long memory, plot result
            if reward > 2 : 
                nwin += 1
            agent.n_games += 1
            agent.train_long_memory()

            if counter < record:
                record = counter
                agent.model.save()

            print('Game', agent.n_games, 'Score', counter, 'Record:', record, 'Max moves:',game.get_max_move())
            if agent.n_games <= 50 : 
                plot_scores.append(counter)
                total_score += counter
                mean_score = total_score / agent.n_games
                plot_mean_scores.append(mean_score)
                plot(plot_mean_scores, plot_scores)
                game.reset()
                counter=0
            else : 
                plot_scores.append(counter)
                mean_score = np.mean(plot_scores[-50:])
                plot_mean_scores.append(mean_score)
                plot(plot_mean_scores, plot_scores)
                game.reset()
                counter=0

        #print(i)
        i+=1

if __name__ == '__main__':
    train()
