# ENVIRONMENT

#import scipy
import Methods
import Random

#global variables (currently all default values)
LAMBDA = 0
THETA_O = 0
THETA_H = 0
THETA_C = 0
N_O = 0
N_H = 0
N_C = 0
list_of_features = []
list_of_agents = []
list_of_games = []
number_of_objs = 0
number_of_games = 0
number_of_agents = 0
agent_ID_count = 0
feature_ID_count = 0
feature_means = []

#matrix to store lexicon x lexicon use/success values
LEXICAL_MATRIX = [[[0,0] for x in range(number_of_agents)] for y in range(number_of_agents)]

#code
for game in range(number_of_games):     #for every game create the right amount of certain features
    list_of_objs =  []
    obj_ID_count = 0
    
    #create NO features
    for f in range(N_O):
        list_of_features.append(Methods.createNOFeature(feature_ID_count))
        feature_ID_count += 1
    
    #create NH features
    for f in range(N_H):
        list_of_features.append(Methods.createNHFeature(feature_ID_count))
        feature_ID_count += 1
        
    #create NC features
    for f in range(N_C):
        list_of_features.append(Methods.createNCFeature(feature_ID_count))
        feature_ID_count += 1
    
    #create an object with the features generated    
    for obj in range(number_of_objs):
        list_of_objs.append(Methods.createObj(obj_ID_count, list_of_features))
        obj_ID_count += 1
        
    #add the game to the list of games
    list_of_games.append(list_of_objs)

#create all agents and add them to a list    
for agent in range(number_of_agents):
    list_of_agents.append(Methods.createAgent(agent_ID_count, list_of_features))
    agent_ID_count += 1    
    
#randomly select an agent
selected_agent = Random.choice(list_of_agents)

#randomly select a game
selected_game = Random.choice(list_of_games)

#randomly select an object
selected_object = Random.choice(selected_game)

#randomly select a feature
selected_feature = Random.choice(selected_object.features)

#randomly select a listening agent
listening_agent = Random.choice(list_of_agents)


#.......

#assign success value (1 if successful, 0 if not)
if (successful):
    succ_pt = 1
else:
    succ_pt = 0
    
#get the current use_success values
selected_agent_use_succ = LEXICAL_MATRIX[selected_agent.ID][listening_agent.ID]

#create a new use_success list increasing the use by 1 and success by 1 if successful
new_use_succ = [selected_agent_use_succ[0] + 1, selected_agent_use_succ[1] + succ_pt]

#assign the new values to the matrix
LEXICAL_MATRIX[selected_agent.ID][listening_agent.ID] = new_use_succ
 
