#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#uses results from greedy algorithm
#algorithm to classify each sequence

import os, random
import pandas as pd


def classify(motifs, data):

    #signify if the sequence is good (+1) or bad (-1)
    good = False
    count = 0

    sequences = list(data.index)

    #keeps track of our classifications
    classes = dict((key,0) for key in sequences)
    #classes = pd.DataFrame(columns = [motifs], index = [columns])

    #loop through all testing sequences (random 1/3 of data)
    for sequence in sequences:
        count += 1
        #loop through "good" motifs - classifed by greedy algorithm
        for m in motifs:
            #if sequence contains motif
            if data.at[sequence, m] == 1:
                good = True
                continue
        if good == True:
            #one+ good motif found in sequnce classify as +1
            if count < 6:
                print("Classifier: " + sequence + " is Class +1")
            classes[sequence] = 1
        elif good == False:
            #no good motifs found in sequence, classify as -1
            if count < 6:
                print("Classifier: " + sequence + " is Class -1")
            classes[sequence] = -1
        good = False

    return classes




