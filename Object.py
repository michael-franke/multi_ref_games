#OBJECT

class Obj(object):
    def __init__(self, *args):
        self.ID = 0             #every object has a unique ID for referencing
        self.features = []      #list of features the object has