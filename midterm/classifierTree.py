#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#uses results from decision tree
#algorithm to classify each sequence

import os, random
import pandas as pd


def classify(motifs, data, tree):

    #signify if the sequence is good (+1) or bad (-1)
    count = 0
    path = ""

    sequences = list(data.index)

    #keeps track of our classifications
    classes = dict((key,0) for key in sequences)
    #classes = pd.DataFrame(columns = [motifs], index = [columns])

    #loop through all testing sequences (random 1/3 of data)
    for sequence in sequences:
        #ROOT present
        if data.at[sequence, motifs[0]] == 1:
            path = "1"
            #LEFT CHILD present
            if data.at[sequence, motifs[1]] == 1:
                path += "1"
                #LEFT LEFT CHILD present
                if tree.at["Foreground", "LeftLeftChild"] > tree.at["Background", "LeftLeftChild"]:
                    path += "+1"
                #LEFT LEFT CHILD not prestnt
                else:
                    path += "-1"
            #LEFT CHILD not present
            elif data.at[sequence, motifs[1]] == 0:
                path += "0"
                #LEFT RIGHT CHILD present
                if tree.at["Foreground", "LeftRightChild"] > tree.at["Background", "LeftRightChild"]:
                    path += "+1"
                    #LEFT RIGHT CHILD not present
                else:
                    path += "-1"
        #ROOT not present
        elif data.at[sequence, motifs[0]] == 0:
            path = "0"
            #RIGHT CHILD present
            if data.at[sequence, motifs[2]] == 1:
                path += "1"
                #RIGHT LEFT CHILD present
                if tree.at["Foreground", "RightLeftChild"] > tree.at["Background", "RightLeftChild"]:
                    path += "+1"
                #RIGHT LEFT CHILD not prestnt
                else:
                    path += "-1"
            #RIGHT CHILD not present
            elif data.at[sequence, motifs[2]] == 0:
                path += "0"
                #RIGHT RIGHT CHILD present
                if tree.at["Foreground", "RightRightChild"] > tree.at["Background", "RightRightChild"]:
                    path += "+1"
                    #RIGHT RIGHT CHILD not present
                else:
                    path += "-1"

        count += 1
        #print("Path: " + path)
        result = path[2]
       # print(result)
        if result == "+":
            #one+ good motif found in sequnce classify as +1
            classes[sequence] = 1
            if count < 6:
                print("\nClassifier: " + sequence)
                print("Path: " + path + "\tClass: +1")
        elif result == "-":
            #no good motifs found in sequence, classify as -1
            classes[sequence] = -1
            if count < 6:
                print("\nClassifier: " + sequence)
                print("Path: " + path + "\tClass: -1")

    return classes




