# ENVIRONMENT

import scipy
import numpy
import itertools
import Methods
import Random

#global variables (currently all default values)
LAMBDA = 4
THETA_O = [5,5] # shape parameters for a beta distribution; for open scales
THETA_H = [0.95,1] # shape parameters for a beta distribution; for half-open scales
THETA_C = [1,1] # shape parameters for a beta distribution; for closed scales
N_O = 2
N_H = 2
N_C = 2
list_of_features = [] # maybe not necessary?
list_of_agents = []   # maybe not necessary?
list_of_games = []
number_of_games = 100
number_of_objs = 0    # not necessary (sampled in for each context)
number_of_agents = 0  # we don't actually have agents, strictly speaking
agent_ID_count = 0    # see above
feature_ID_count = 0  # ???
feature_means = []    # ???

## LEXICA:
## for each property type (open, half-open, closed), we have two words (high and low)
## examples:
lexicon_1= numpy.array([[0.1,0.9],
                       [0.3,0.7],
                       [0.4,0.8]])
lexicon_2= numpy.array([[0.3,0.4],
                       [0.2,0.6],
                       [0.4,0.6]])
# TO DO: create the set of all possible lexica (using values 0, 0.1, ... 0.9, 1)

#matrix to store lexicon x lexicon use/success values
AVERAGE_UTIL_MATRIX = [[[0,0] for x in range(number_of_lexica)] for y in range(number_of_lexica)]

#code
for game in range(number_of_games):     #for every game create the right amount of certain features
    # sample number of objects in context
    number_of_objects = numpy.random.poisson(LAMBDA,1)[0] + 2
    # sample a context (by sampling features for each object
    context = numpy.concatenate([numpy.random.beta(THETA_O[0], THETA_O[1], [number_of_objects, N_O]),
                                 numpy.random.beta(THETA_H[0], THETA_H[1], [number_of_objects, N_H]),
                                 numpy.random.beta(THETA_C[0], THETA_C[1], [number_of_objects, N_C])], axis = 1)
    #add the game to the list of games
    list_of_games.append(context)

## messed with the code up to here

#create all agents and add them to a list    
for agent in range(number_of_agents):
    list_of_agents.append(Methods.createAgent(agent_ID_count, list_of_features))
    agent_ID_count += 1    
    
#randomly select an agent
selected_agent = Random.choice(list_of_agents)

#randomly select a game
selected_game = Random.choice(list_of_games)

#randomly select an object
selected_object = Random.choice(selected_game)

#randomly select a feature
selected_feature = Random.choice(selected_object.features)

#randomly select a listening agent
listening_agent = Random.choice(list_of_agents)


#.......

#assign success value (1 if successful, 0 if not)
if (successful):
    succ_pt = 1
else:
    succ_pt = 0
    
#get the current use_success values
selected_agent_use_succ = LEXICAL_MATRIX[selected_agent.ID][listening_agent.ID]

#create a new use_success list increasing the use by 1 and success by 1 if successful
new_use_succ = [selected_agent_use_succ[0] + 1, selected_agent_use_succ[1] + succ_pt]

#assign the new values to the matrix
LEXICAL_MATRIX[selected_agent.ID][listening_agent.ID] = new_use_succ
 
