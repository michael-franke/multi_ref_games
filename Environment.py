# ENVIRONMENT

import numpy
import random
#import time

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
    #print("number of objects: ", number_of_objects)
    context = numpy.concatenate([numpy.random.beta(THETA_O[0], THETA_O[1], [number_of_objects, N_O]),
                                 numpy.random.beta(THETA_H[0], THETA_H[1], [number_of_objects, N_H]),
                                 numpy.random.beta(THETA_C[0], THETA_C[1], [number_of_objects, N_C])], axis = 1)
    return context
 


def get_lexica(stepsize = 1.0/3):
    all_lexica = []
    o1 = [0.3,0.7]
    h1 = [0.3,0.7]
    c1 = [0.3,0.7]
    
    o2 = [0.5,0.5]
    h2 = [0.5,0.5]
    c2 = [0.5,0.5]
    
    features = [o1,h1,c1]
    all_lexica.append(features)
    features = [o2,h2,c2]
    all_lexica.append(features)
                            
    return all_lexica

#def normalize(m): #check this
#    m = m / m.sum(axis=1)[:, numpy.newaxis]
#    m[numpy.isnan(m)] = 0.
#    return m

def semantics(g, L):
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
    m = numpy.longdouble(speakerChoice)
    m = m / m.sum(axis=1)[:, numpy.newaxis]
    m[numpy.isnan(m)] = 1.0/len(m[0])
    
    return m


def printLexica():
    print("==========================")
    print("LEXICA")
    
    for lexica in list_of_lexica:
        print("\t| low \t| high")
        print("--------------------------")
        print("Open\t| ", lexica[0][0], "| ", lexica[0][1])
        print("Half\t| ", lexica[1][0], "| ", lexica[1][1])
        print("Closed\t| ", lexica[2][0], "| ", lexica[2][1])
        print("==========================")
        print()

def printGames():
    string = "===================================================================================================================\n"
    string += "GAMES\n"
    
    for gameIdx in range(len(list_of_games)):
        string += "Game\t| Object\t"
        for features in range(len(list_of_games[gameIdx][0])):
            string += "| value "
            string += str(features)
            string += "\t "
        
        string += "--------------------------------------------------------------------------------------------------------------------\n"
        
    
        string += "Game"
        string += str(gameIdx)
        for objIdx in range(len(list_of_games[gameIdx])):
            string += "\t| Object"
            string += str(objIdx)
            string += "\t"
            for features in range(len(list_of_games[gameIdx][objIdx])):
                string += "| "
                string += str(list_of_games[gameIdx][objIdx][features])[:5]
                string += "\t\t"
            
            string += "\n"
        string += "====================================================================================================================\n"

    print(string)


def printSem(sem):
    string = "=====================================================================================================\n"
    string += "SEMANTICS\n"
    string += "Object\t"
    
    for features in range(0,len(sem[0]),2):
        string += "| f_"
        string += str(int(features/2))
        string += "\t\t"
    string += "\n\t"
    
    for messages in range(0,len(sem[0]),2):
        string += "| low\t| high\t"
        
    string += "\n---------------------------------------------------------------------------------------------------\n"
    
    for objIdx in range(len(sem)):
        string += "Object"
        string += str(objIdx)
        string += "\t"
        for valueIdx in range(len(sem[objIdx])):
            string += "| "
            string += str(sem[objIdx][valueIdx])
            string += "\t"
        string += "\n"
        
    string += "=====================================================================================================\n"
    
    print(string)


def printCP(which, cp):
    #cp = numpy.transpose(cp)
    print(cp, len(cp), len(cp[0]))
    
    string = "=======================================================================\n"
    string += "CHOICE_PROBABILITY: "
    string += which
    string += "\nObject\t"
    
    for featIdx in range(0,len(cp[0]),2):
        string += "| f_"
        string += str(int(featIdx/2))
        string += "\t\t"
    string += "\n\t"
    
    for messages in range(0,len(cp[0]),2):
        string += "| low\t| high\t"
        
    string += "\n--------------------------------------------------------------------\n"     
    
    for objIdx in range(len(cp)):
        string += "obj_"
        string += str(objIdx)
        string += "\t"
        
        for featIdx in range(len(cp[objIdx])):
            string += "| "
            string += str(cp[objIdx][featIdx])[:5]
            string += "\t"
        string += "\n"
        
    string += "====================================================================\n"
    
    print(string)
    
    
def printLL(ll):
    string = "=======================================================================\n"
    string += "LITERAL_LISTENER\n"
    string += "feature\t| message\t"
    for featIdx in range(len(ll[0])):
        string += "| Obj"
        string += str(featIdx)
        string += "\t"
    
    string += "\n--------------------------------------------------------------------\n"     
    
    messageCount = 0
    
    for featIdx in range(len(ll)):
        if messageCount == 2:
            messageCount = 0
        if featIdx % 2 == 0:
            string += "f_"
            string += str(int(featIdx/2))
        string += "\t| mess_"
        string += str(messageCount)
        messageCount += 1
        string += "\t"
        
        for objIdx in range(len(ll[featIdx])):
            string += "| "
            string += str(ll[featIdx][objIdx])[:5]
            string += "\t"
        string += "\n"
        
        
        
    string += "====================================================================\n"
    
    print(string)
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
#print("lexica: ", list_of_lexica)
    

#matrix to store lexicon x lexicon use/success values
AVERAGE_UTIL_MATRIX = [[[0,0] for x in range(number_of_lexica)] for y in range(number_of_lexica)]
#print("AVERAGE_UTIL_MATRIX: ", AVERAGE_UTIL_MATRIX)




#code
for game in range(number_of_games):     #for every game create the right amount of certain features
    context = get_context()
    #add the game to the list of games
    list_of_games.append(context)

#print("list of games: ", list_of_games[0])  

g = random.choice(list_of_games)
#print("g: ", g)

Lj = random.choice(list_of_lexica)
#print("Lj: ", Lj)

printLexica()
printGames()    

sem = semantics(g, Lj)
printSem(sem)

literal_listener = normalise(numpy.transpose(sem))
printLL(literal_listener)

speaker_choice = normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
printCP("speaker_choice", speaker_choice)

listener_choice = normalise(numpy.transpose(speaker_choice))
printCP("listener_choice", numpy.transpose(listener_choice))
printLL(listener_choice)

############

def speaker_choice_FUN(g, speaker_lexicon, LAMBDA = 5):
    sem = semantics(g, speaker_lexicon)
    literal_listener = normalise(numpy.transpose(sem))
    speaker_choice = normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
    return speaker_choice

def listener_choice_FUN(game, lexicon, LAMBDA = 5):
    sem = semantics(game, lexicon)
    literal_listener = normalise(numpy.transpose(sem))
    speaker_choice = normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
    listener_choice = normalise(numpy.transpose(speaker_choice))
    return listener_choice

def get_EU(g, speaker_lexicon, listener_lexicon):
    speaker_choice  = speaker_choice_FUN(g,speaker_lexicon)
    listener_choice = listener_choice_FUN(g, listener_lexicon)
    EU = numpy.sum(speaker_choice * numpy.transpose(listener_choice)) / len(g)
    return(EU)

ngames = 1000 # how many games to sample from
EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)]) # matrix with zeros of right size

for s_type in range(len(list_of_lexica)):
    for l_type in range(len(list_of_lexica)):
        EU[s_type, l_type] += numpy.mean([get_EU(get_context(),
                                                 list_of_lexica[s_type],
                                                 list_of_lexica[s_type])
                                          for g in range(ngames)])

print(EU)
# seems like the first lexicon is doing better than the second