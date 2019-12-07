#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#runs the Greedy Algorithm on a 
#set of motif boolean vectors. 
#returns a list of "good" motifs

import sys, os, argparse
import pandas as pd

def greed(data):

    #column names, found motifs
    columns = list(data)

    if "Class" in columns:
        data = data[data.Class == 1]
        data = data.drop("Class", axis = 1)

    columns = list(data)
    motifs = list()
    rows = list(data.index)

    max = 0
    num_cov = 0
    target = len(rows)
    total = len(columns)

    #for sums of motifs
    sums = dict((el,0) for el in columns)

    #for coverage
    covered = dict((el,False) for el in rows)

    #loop through col, adding up sums and adding to list
    for col in columns:
        sums[col] = data[col].sum()

    #row for sums
    dfsums = pd.DataFrame([sums], columns = columns, index = ["Sum"])

    #add row for sum to dataframe
    sdata = data.append(dfsums)

    #initialize first for sums loop
    first = True

    theVariableThatChecksHowMuchMoreCoverageWeCanGetFromThisFile = len(rows) * 0.05

    while num_cov < target:

        #find max coverage
        #print("finding new max...")
        for i in sums:
            if first == True:                   #Sets first maximum value for comparison
                max = sums[i]
                first = False
                mot = i
            else:                               
                if sums[i] > max:               #Checks for maximum coverage
                    max = sums[i]
                    mot = i

        if max < theVariableThatChecksHowMuchMoreCoverageWeCanGetFromThisFile:                            #Checks to see if maximum coverage has been reached
            print("\nGREEDY: Max motif coverege is now lower than 5%.\n Maximum coverage achieved.")
            break
                    
        motifs.append(mot)                      #Adds motif to list of maximum coverage

        #print('deleting key...') #Testing
        del sums[mot]
        del columns[columns.index(mot)]                          #Removes from sums library

        #update covered
        #print("updating coverage...")
        #print(num_cov) #Testing
        for row in rows:                        #Iterates through gene to check coverage
            if covered[row] == False:
                if sdata.at[row, mot] == 1:     #Checks if chosen motif covers current gene
                    covered[row] = True
                    num_cov = num_cov + 1

                    # #NEW
                    # for c in columns:           #replace covered values in sdata with 0s
                    #     sdata.at[row, c] = 0

        #reset sums to uncovered
        for c in columns:                       #Iterates through motifs
            sums[c] = 0
            for r in rows:
                if covered[r] == False:         #Checks if gene has been covered by motif
                    if sdata.at[r, c] == 1:     #Checks if current motif covers gene
                        sums[c] = sums[c] + 1



        #NEW
        #reset sums to uncovered
        #print("resetting sums..")
        # for col in columns:                     #recalculating sums
        #     sums[col] = sdata[col].sum()


        first = True #reinitializes first max

        if total == len(motifs):                       #Checks if all motifs have been covered
            print("\nGREEDY: All Motif's used.\n Maximum covereage achieved.")
            break

    if(max == 0):
        print("GREEDY: Full coverage acheived.\n")

    return motifs




