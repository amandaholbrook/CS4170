#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#creates a random forest out 
#of a set of motif boolen vectors. 
#returns the tree of best motifs.

# import ray
# import modin.pandas as pd
# import os
from computePhi import phi
from decisionTree import tree
from math import sqrt
import pandas as pd
import random


def forest(data1):

    data = data1.drop('Class', axis = 1)
    rows = list(data.index)
    columns = list(data)

    avg = 0

    trees = []
    roots = list()
    left = list()
    right = list()
    row = pd.DataFrame()

    for x in range (1, 26):
        
        #bootstrapped sample
        #select random sample size N = 14000
        row = data.sample(frac = 1, replace = True, axis = 0, random_state= random.randint(1, 100000000))

        # for r in range (0, len(rows)):
        #     row = row.append(data.sample())


        #select random subset of features size sqrt(N) = sqrt(107)
        sr = int(sqrt(len(columns)))
        bootstrap = row.sample(n = sr, axis = 1)

        drops = list(bootstrap.index)

        #rename all duplicates
        bootstrap.index = bootstrap.index + bootstrap.groupby(level=0).cumcount().astype(str).replace('0','')

        outOfBag = data.drop(drops)
        avg += len(outOfBag.index)

        # outOfBag.to_csv(bag)

        c = pd.DataFrame(data1['Class'])
        bootstrap = bootstrap.join(c)

        # bootstrap.to_csv(boot)

        #construct decision trees
        decisionTree = tree(bootstrap)
        roots.append(decisionTree.at['Motif', 'Root'])
        left.append(decisionTree.at['Motif', 'LeftChild'])
        right.append(decisionTree.at['Motif', 'RightChild'])
        if x < 6:
            print('\nTree ' + str(x))
            print("Root Feature: " + decisionTree.at['Motif', 'Root'])
            print("Out of Bag Size: " + str(len(outOfBag.index)))

        trees.append(decisionTree)

    avg = int(avg / x)
    print("\nAverage out of bag size: " + str(avg) + "\n")

    return trees, roots, left, right