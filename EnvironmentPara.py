import os
import numpy
import Methods
import time

from joblib import Parallel, delayed
from joblib import load, dump


def g_adder(n, EU, games, list_of_lexica):
    print("enter")
    LAMBDA = 5
    THETA_O = [5,5] # shape parameters for a beta distribution; for open scales
    THETA_H = [0.95,1] # shape parameters for a beta distribution; for half-open scales
    THETA_C = [1,1] # shape parameters for a beta distribution; for closed scales
    N_O = 2
    N_H = 2
    N_C = 2
    print("1")
    game = Methods.get_context(LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C)
    print("2")
    EU_local = Methods.get_EU(game, list_of_lexica, LAMBDA, N_O, N_H, N_C)/games
    print("3")
    return EU_local

if __name__ == "__main__":
    startTime = time.time()
    nSteps = 4    # this is 1/n
    ngames = 5 # how many games to sample from
    list_of_lexica = Methods.get_all_lexica(nSteps)
    print("a")
    EU = numpy.zeros([len(list_of_lexica), len(list_of_lexica)])
    #print(EU)
    results = Parallel(n_jobs=8)(delayed(g_adder)(i, EU, ngames, list_of_lexica) for i in list(range(ngames)))
    print(results)
    print((time.time() - startTime)/60, " min")
