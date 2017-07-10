# ENVIRONMENT

import numpy
#import random
import Methods
import printMethods
#import time

#global variables (currently all default values)
LAMBDA = 5
THETA_O = [5,5] # shape parameters for a beta distribution; for open scales
THETA_H = [0.95,1] # shape parameters for a beta distribution; for half-open scales
THETA_C = [1,1] # shape parameters for a beta distribution; for closed scales
N_O = 2
N_H = 2
N_C = 2
list_of_lexica = []
#list_of_games = []
nSteps = 3    # this is 1/n
ngames = 100  # how many games to sample from




### LEXICA - only 2 ###

#list_of_lexica = Methods.get_lexica()

########

### LEXICA - ALL possible lexica ####

list_of_lexica = Methods.get_all_lexica(nSteps) #WARNING: this takes a LONG time to process in later methods

################


##### code for sampling games ######

# create vector of 'ngames' games/contexts
# games = [Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C) for g in range(ngames)]

# matrix with zeros of right size to fill in EU values
EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)])

for g_count in range(ngames):
    game = Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C)
    EU += Methods.get_EU(game, list_of_lexica, LAMBDA, N_O, N_H, N_C)/ngames

print("EU: ", EU)