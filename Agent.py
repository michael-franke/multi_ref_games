#AGENT

class Agent(object):
    def __init__(self, *args):
        self.ID = 0             #Every agent has a unique ID which can be used in lookups
        self.lexicon = {}       #lexicon of low-high thresholds. {feature : [low, high]}