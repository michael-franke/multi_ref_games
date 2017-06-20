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
nSteps = 3   # this is 1/n 
ngames = 1000 # how many games to sample from




### LEXICA - only 2 ###

#list_of_lexica = Methods.get_lexica()

########

### LEXICA - ALL possible lexica ####

list_of_lexica = Methods.get_all_lexica(nSteps) #WARNING: this takes a LONG time to process in  later methods

################    


##### code for ALL games at once #####
#for game in range(number_of_games):     #for every game create the right amount of certain features
    #context = Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C)
    #add the game to the list of games
    #list_of_games.append(context)

#print("list of games: ", list_of_games[0])  

#g = random.choice(list_of_games)
#print("g: ", g)

#Lj = random.choice(list_of_lexica)
#print("Lj: ", Lj)

#printMethods.printLexica(list_of_lexica)
#printMethods.printGames(list_of_games)    

#sem = Methods.semantics(g, Lj)
#printMethods.printSem(sem)

#literal_listener = Methods.normalise(numpy.transpose(sem))
#printMethods.printLL(literal_listener)

#speaker_choice = Methods.normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
#printMethods.printCP("speaker_choice", speaker_choice)

#listener_choice = Methods.normalise(numpy.transpose(speaker_choice))
#printMethods.printCP("listener_choice", numpy.transpose(listener_choice))
#printMethods.printLL(listener_choice)

############


##### code for sampling games ######

EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)]) # matrix with zeros of right size

for s_type in range(len(list_of_lexica)):
    for l_type in range(len(list_of_lexica)):
        EU[s_type, l_type] += numpy.mean([Methods.get_EU(Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C),
                                                 list_of_lexica[s_type],
                                                 list_of_lexica[s_type], 
                                                 LAMBDA, N_O, N_H, N_C)
                                          for g in range(ngames)])

print("EU: ", EU)
# seems like the first lexicon is doing better than the second
