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
ngames = 1000  # how many games to sample from




### LEXICA - only 2 ###

#list_of_lexica = Methods.get_lexica()

########

### LEXICA - ALL possible lexica ####

list_of_lexica = Methods.get_all_lexica(nSteps) #WARNING: this takes a LONG time to process in  later methods
list_of_lexica = list_of_lexica[0:100]

################    


##### code for sampling games ######

# create vector of 'ngames' games/contexts
games = [Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C) for g in range(ngames)]

# get a speaker and listener behavior for each of these games for each lexicon
behavior = [ [ Methods.get_speakerlistener_FUN(game, lexicon, LAMBDA, N_O, N_H, N_C) for game in games]
                        for lexicon in list_of_lexica]

# matrix with zeros of right size to fill in EU values
EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)])

# get EU values
for lrow in range(len(list_of_lexica)):
    for lcol in range(len(list_of_lexica)):
        if lcol < lrow:
            EU[lrow, lcol] = EU[lcol, lrow] # if we have calculated this before, reuse value
        else:
            EU[lrow, lcol] = 0.5 * numpy.mean([ Methods.get_EU_behavior(games[game_index],
                                                                behavior[lrow][game_index][0],
                                                                behavior[lcol][game_index][1]) + \
                                                Methods.get_EU_behavior(games[game_index],
                                                                behavior[lcol][game_index][0],
                                                                behavior[lrow][game_index][1])
                                                for game_index in range(len(games))])

print("EU: ", EU)
