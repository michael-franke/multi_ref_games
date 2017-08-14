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
    
    
    def saveData(i, startTime, list_of_lexica, results, LAMBDA, THETA_O, THETA_H, THETA_C, N_O, N_H, N_C, nStep, ngames):
        if not os.path.exists(''.join(["C:/Users/Richard Belk/OneDrive/SFS WORK/Reports/"])):
            os.makedirs(''.join(["C:/Users/Richard Belk/OneDrive/SFS WORK/Reports/"]))
                     
        reportfile = ''.join(["C:/Users/Richard Belk/OneDrive/SFS WORK/Reports/report_", datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S"), ".txt"])
        reporttxt = "EU REPORT- section: "
        reporttxt += str(i)
        reporttxt += "\n"
        reporttxt += "Runtime: "
        reporttxt += str("%.4f" % ((time.time() - startTime) / 60))
        reporttxt += " minutes\n"
        reporttxt += "LAMBDA: "
        reporttxt += str(LAMBDA)
        reporttxt += "\nTHETA_O: "
        reporttxt += str(THETA_O)
        reporttxt += "\nTHETA_H: "
        reporttxt += str(THETA_H)
        reporttxt += "\nTHETA_C: "
        reporttxt += str(THETA_C)
        reporttxt += "\nN_O: "
        reporttxt += str(N_O)
        reporttxt += "\nN_H: "
        reporttxt += str(N_H)
        reporttxt += "\nN_C: "
        reporttxt += str(N_C)
        reporttxt += "\nnStep: "
        reporttxt += str(nStep)
        reporttxt += "\nngames: "
        reporttxt += str(ngames)
        reporttxt += "\n\n"

        reporttxt += printLexica(list_of_lexica)
    
        reporttxt += "\n\nEU\n"
    
        #reporttxt +=  (repr(results))
        for x in results:
            for y in x:
                reporttxt += str(y) + "\t"
            reporttxt += "\n"
        reporttxt += "\n"
        
        text_file = open(reportfile, "w")
        text_file.write(reporttxt)
        text_file.close()  
