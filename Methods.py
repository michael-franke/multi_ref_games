import numpy


def get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C):
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

def semantics(g, L, N_O, N_H, N_C):
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

def speaker_choice_FUN(g, speaker_lexicon, LAMBDA, N_O, N_H, N_C):
    sem = semantics(g, speaker_lexicon, N_O, N_H, N_C)
    literal_listener = normalise(numpy.transpose(sem))
    speaker_choice = normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
    return speaker_choice

def listener_choice_FUN(game, lexicon, LAMBDA, N_O, N_H, N_C):
    sem = semantics(game, lexicon, N_O, N_H, N_C)
    literal_listener = normalise(numpy.transpose(sem))
    speaker_choice = normalise(numpy.exp(LAMBDA * numpy.transpose(literal_listener)))
    listener_choice = normalise(numpy.transpose(speaker_choice))
    return listener_choice

def get_EU(g, speaker_lexicon, listener_lexicon, LAMBDA, N_O, N_H, N_C):
    speaker_choice  = speaker_choice_FUN(g,speaker_lexicon, LAMBDA, N_O, N_H, N_C)
    listener_choice = listener_choice_FUN(g, listener_lexicon, LAMBDA, N_O, N_H, N_C)
    EU = numpy.sum(speaker_choice * numpy.transpose(listener_choice)) / len(g)
    return(EU)
