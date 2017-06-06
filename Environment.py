# ENVIRONMENT

import numpy
import random
import time

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
number_of_objects = -1

def get_context():
    number_of_objects = numpy.random.poisson(LAMBDA,1)[0] + 2
    # sample a context (by sampling features for each object
    print("number of objects: ", number_of_objects)
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

#def normalize(m): #check this
#    m = m / m.sum(axis=1)[:, numpy.newaxis]
#    m[numpy.isnan(m)] = 0.
#    return m

def speaker_choice(g, L):
    #print("len(g): ", len(g))
    #print("leng0: ", len(g[0]))
    semantics = [[-1 for features in range(2 * len(g[0]))] for objs in range(len(g))]
    #print("semantics: ", semantics)
    feature_count = 0
    
    for j in range(len(g)):
        feature_count = 0
        for i in range(N_O):
            #print("g[][]: ", g[j][i])
            #print("L[]: ", L[0])
            #print("ij: ", i, j, feature_count)
            if g[j][i] < L[0][0]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            
            if g[j][i] > L[0][1]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            #print("semantics2: ", semantics)
        #print("featurecount: ", feature_count)    
        for i in range(N_O, N_O + N_H):
            #print("ij: ", i, j, feature_count)
            #print("g[][]: ", g[j][i])
            #print("L[]: ", L[0])
            if g[j][i] < L[1][0]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            
            if g[j][i] > L[1][1]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            #print("semantics2: ", semantics)
        #print("featurecount: ", feature_count)    
        for i in range(N_O + N_H, N_O + N_H + N_C):
            #print("ij: ", i, j, feature_count)
            #print("g[][]: ", g[j][i])
            #print("L[]: ", L[0])
            if g[j][i] < L[2][0]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            
            if g[j][i] > L[2][1]:
                semantics[j][feature_count] = 1
            else:
                semantics[j][feature_count] = 0
            feature_count += 1
            #print("semantics2: ", semantics)
            
    return semantics
 
def normalise(speakerChoice):
    

    shared_value = 0
    feature_values = []
    print("speakerchoice: ", len(speakerChoice))
    print("speakerchoice0: ", len(speakerChoice[0]))
    literal_listener = [[-1 for features in range(len(speakerChoice))] for objs in range(len(speakerChoice[0]))]
    #print("Llistener: ", literal_listener)
    for i in range(len(speakerChoice[0])):
        true_count = []
        for j in range(len(speakerChoice)):
            true_count.append(speakerChoice[j][i])
        print("true_count: ", true_count)
        shared_value = 1.0 / numpy.sum(true_count)
        feature_values.append(shared_value)
        print("feature_values: ", feature_values)

    for i in range(len(speakerChoice[0])):
        for j in range(len(speakerChoice)):
            if speakerChoice[j][i] == 1:
                literal_listener[i][j] = feature_values[i]
            else:
                literal_listener[i][j] = 0
    
    for i in range(len(literal_listener)):
        if numpy.sum(literal_listener[i]) == 0:
            #print("triggered", i)
            for k in range(len(literal_listener[i])):
                literal_listener[i][k]= 1.0 / len(literal_listener[i])
            #print(literal_listener[i])
    print("literal_L: ", literal_listener)     
    
    for j in range(len(literal_listener)):
        x = numpy.array(literal_listener[j])
        print("x: ", x)
        y = numpy.exp(LAMBDA * x)
        print("y: ", y)
        choice_probability = y / numpy.sum(y)

    
           
    #semantics = [[ truth-value of whether m is true of o given L for m in M] for o in g]
    #literal_listener = normalize(numpy.transpose(semantics))
    #choice_probability = numpy.exp(LAMBDA * literal_listener[:,0])
    #choice_probability = choice_probability / numpy.sum(choice_probability)
    
    return choice_probability
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

print("list of games: ", list_of_games[0])  

g = random.choice(list_of_games)
print("g: ", g)

Lj = random.choice(list_of_lexica)
print("Lj: ", Lj)
    
speakerChoice = speaker_choice(g, Lj)
choice_probability = normalise(speakerChoice)

#print("speakerChoice: ", speakerChoice)
print("choice_probability: ", choice_probability)    
