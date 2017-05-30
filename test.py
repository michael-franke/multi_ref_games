# ENVIRONMENT

import numpy
import random

#global variables (currently all default values)
LAMBDA = 4
THETA_O = [5,5] # shape parameters for a beta distribution; for open scales
THETA_H = [0.95,1] # shape parameters for a beta distribution; for half-open scales
THETA_C = [1,1] # shape parameters for a beta distribution; for closed scales
N_O = 2
N_H = 2
N_C = 2
list_of_lexica = []
list_of_games = []
number_of_games = 2
number_of_lexica = 2

def get_context():
    number_of_objects = numpy.random.poisson(LAMBDA,1)[0] + 2
    # sample a context (by sampling features for each object
    context = numpy.concatenate([numpy.random.beta(THETA_O[0], THETA_O[1], [number_of_objects, N_O]),
                                 numpy.random.beta(THETA_H[0], THETA_H[1], [number_of_objects, N_H]),
                                 numpy.random.beta(THETA_C[0], THETA_C[1], [number_of_objects, N_C])], axis = 1)
    return context
 


def get_lexica():
    all_lexica = []
    o1 = [0.9,0.6]       
    h1 = [0.3,0.7]
    c1 = [0.4,0.8]
    
    o2 = [0.3,0.4]     
    h2 = [0.2,0.6]
    c2 = [0.4,0.6]
    
    features = [o1,h1,c1]
    all_lexica.append(features)
    features = [o2,h2,c2]
    all_lexica.append(features)
                            
    return all_lexica



             
### pseudo

def normalize(m):
    m = m / m.sum(axis=1)[:, numpy.newaxis]
    m[numpy.isnan(m)] = 0.
    return m

def speaker_choice(g, L):
    print("len(g): ", len(g))
    print("leng0: ", len(g[0]))
    semantics = [[[-1,-1] for features in range(len(g[0]))] for objs in range(len(g))]
    print("semantics: ", semantics)
    cell = []
    low = -1
    high = -1
    lexicon_count = 0
    
    for i in range(len(g)):
        g_obj = g[i]
        print("g_obj: ", g_obj)
        for j in range(len(g_obj)):
            g_feature = g_obj[j]
            print("g_feature: ", g_feature)
            L_feature = L[lexicon_count]
            print("L_feature: ", L_feature)
            if (g_feature < L_feature[0]):
                low = 1
            else:
                low = 0
                
            if(g_feature > L_feature[1]):
                high = 1
            else:
                high = 0
                
            cell = [low,high]
            semantics[i][j] = cell
            lexicon_count += 1
    
    
    
    
    #semantics = [[ truth-value of whether m is true of o given L for m in M] for o in g]
    literal_listener = normalize(numpy.transpose(semantics))
    choice_probability = numpy.exp(LAMBDA * literal_listener[:,0])
    choice_probability = choice_probability / numpy.sum(choice_probability)
    
    return (choice_probability)
## LEXICA:
## for each property type (open, half-open, closed), we have two words (high and low)
## examples:
#lexicon_1= numpy.array([[0.9,0.6],
#                       [0.3,0.7],
#                       [0.4,0.8]])
#lexicon_2= numpy.array([[0.3,0.4],
#                       [0.2,0.6],
#                       [0.4,0.6]])
# TO DO: create the set of all possible lexica (using values 0, 0.1, ... 0.9, 1)
list_of_lexica = get_lexica()
print("lexica: ", list_of_lexica)


#matrix to store lexicon x lexicon use/success values
AVERAGE_UTIL_MATRIX = [[[0,0] for x in range(number_of_lexica)] for y in range(number_of_lexica)]
print("AVERAGE_UTIL_MATRIX: ", AVERAGE_UTIL_MATRIX)




#code
for game in range(number_of_games):     #for every game create the right amount of certain features
    context = get_context()
    #add the game to the list of games
    list_of_games.append(context)

print("list of games: ", list_of_games)  

g = random.choice(list_of_games)
print("g: ", g)

Lj = random.choice(list_of_lexica)
print("Lj: ", Lj)
    
speakerChoice = speaker_choice(g, Lj)



  



print("speakerChoice: ", speakerChoice)
    






