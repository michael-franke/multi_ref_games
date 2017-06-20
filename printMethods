def printLexica(list_of_lexica):
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

def printGames(list_of_games):
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
