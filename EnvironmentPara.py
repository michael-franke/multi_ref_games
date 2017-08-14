import os
import numpy
import Methods
import time
import printMethods

from joblib import Parallel, delayed
from joblib import load, dump


def g_adder(startTime, i, nSteps, ngames, list_of_lexica, LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C):
    game = Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C)
    EU_local = Methods.get_EU(game, list_of_lexica, LAMBDA, N_O, N_H, N_C)/ngames
    printMethods.saveData(i, startTime, list_of_lexica, EU_local, LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C, nSteps, ngames)
    
    return EU_local

if __name__ == "__main__":
    startTime = time.time()
    LAMBDA = 5
    THETA_O = [5,5] # shape parameters for a beta distribution; for open scales
    THETA_H = [0.95,1] # shape parameters for a beta distribution; for half-open scales
    THETA_C = [1,1] # shape parameters for a beta distribution; for closed scales
    N_O = 2
    N_H = 2
    N_C = 2
    nSteps = 3   # this is 1/n
    ngames = 10  # how many games to sample from
    list_of_lexica = Methods.get_all_lexica(nSteps)

    #EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)])

    results = Parallel(n_jobs=8)(delayed(g_adder)(startTime, i, nSteps, ngames, list_of_lexica, LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C) for i in list(range(ngames)))
    print((time.time() - startTime)/60, " min")
    
    #printMethods.saveData(startTime, list_of_lexica, results, LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C, nSteps, ngames)
