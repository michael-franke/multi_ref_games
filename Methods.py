# METHODS

import Random
import Object
import Feature
import copy
import Agent

#create an agent with a unique ID and a list of features
def createAgent(agent_ID_count, list_of_features):
    agent = Agent.Agent()
    agent.ID = agent_ID_count
    
    for feature in list_of_features:
        agent.Lexicon[feature.ID] = [0.3, 0.7]
        
    return agent


#create a NO feature with unique ID   
def createNOFeature(THETA_O, feature_ID_count):
    feature = Feature.Feature()
    feature.ID = feature_ID_count
    feature.value = Random.randint(100)
    
    return feature
    

#create a NH feature with unique ID   
def createNHFeature(THETA_H, feature_ID_count):
    feature = Feature.Feature()
    feature.ID = feature_ID_count
    feature.value = Random.randint(100)
    
    return feature


#create a NC feature with unique ID   
def createNCFeature(THETA_C, feature_ID_count):
    feature = Feature.Feature()
    feature.ID = feature_ID_count
    feature.value = Random.randint(100)
    
    return feature


#create an object with a unique ID and list of features
def createObj(obj_ID_count, list_of_features):
    features_list = copy.deepcopy(list_of_features)
    obj = Object.Obj()
    obj.ID = obj_ID_count
    obj.features = features_list
    
    return obj
