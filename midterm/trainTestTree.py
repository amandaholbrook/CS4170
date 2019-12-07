#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#runs a three fold test 
#on the decision tree algorithm

import os, random
import pandas as pd
from classifierTree import classify
from computePhi import phi
from decisionTree import tree
#from decisionTree import tree


#getting data file into dataframe
infile = input("Input testing file: ")
data = pd.read_csv(infile, index_col = 0)
rows = list(data.index)

treeResult = open("treeresults.csv", "w")
classifyResult = open("classifyresults.csv", "w")

tp = fp = tn = fn = accy = err = sens = spec = 0
tot_tp = 0
tot_fp = 0 
tot_tn = 0
tot_fn = 0
tot_accy = 0
tot_err = 0
tot_sens = 0
tot_spec = 0

# one = int(len(rows) / 3)
# test = data.sample(n = one, axis = 0)


# results = tree(test)

# results.to_csv(result)

for trial in range(1, 4):
    #one third of data size
    one = int(len(rows) / 10)

    #dataframe of random one thirds for testing
    test = data.sample(n = one, axis = 0)
    drops = list(test.index)

    #dataframe of remainging two thirds for training
    train = data.drop(drops)

    treeTest = tree(test)
    treeTest.to_csv(treeResult)

    print("\nRoot: " + treeTest.at["Motif", "Root"])
    print("Left Child: " + treeTest.at["Motif", "LeftChild"])
    print("Right Child: " + treeTest.at["Motif", "RightChild"])


    motifs = list()

    for x in range (0, 7):
        motifs.append(treeTest.iloc[0, x])

    #dictionary of actual classifications
    keys = list(test.index)
    values = test['Class'].tolist()
    actual = dict(zip(keys, values))

    #call claffifier, returning dictionary of classfied sequences
    tested = classify(motifs, test, treeTest)

    correct = 0
    total = len(test.index)

    # print(len(data))
    # print(len(test))
    # print(len(train))

    #calculating tp, fp, tn, fn
    for i in tested:
        if actual[i] == 1:
            if tested[i] == 1:
                tp += 1
            elif tested[i] == -1:
                fp += 1
        elif actual[i] == -1:
            if tested[i] == 1:
                fn += 1
            elif tested[i] == -1:
                tn += 1


    accy = (tn + tp) / (tn + fn + fp + tp)
    err = (fn + fp) / (tn + fn + fp + tp)
    sens = tp / (tp + fn)
    spec = tn / (fp + tn)
    
    tot_tp += tp
    tot_fp += fp 
    tot_tn += tn
    tot_fn += fn
    tot_accy += accy
    tot_err += err
    tot_sens += sens
    tot_spec += spec

    tp = fp = tn = fn = accy = err = sens = spec = 0

    tp = tot_tp/trial
    fp = tot_fp/trial
    tn= tot_tn/trial
    fn = tot_fn/trial
    accy = tot_accy/trial
    err = tot_err/trial
    sens = tot_sens/trial
    spec = tot_spec/trial

    pfp = fp / (fp + tp)
    pfn = fn / (fn + tn)

    print("\n\nDecision Tree Classifier Trial " + str(trial) + " Results:")
    print('TP: ' + format(tp, '.0f'))
    print('FP: '  + format(fp, '.0f'))
    print('TN: '  + format(tn, '.0f'))
    print('FN: '  + format(fn, '.0f'))
    print('PFP: '  + format(pfp, '.2f'))
    print('PFN: '  + format(pfn, '.2f'))
    print('Accuracy: '  + format(accy, '.2f'))
    print('Error Rate: '  + format(err, '.2f'))
    print('Sensitivity: '  + format(sens, '.2f'))
    print('Specificity: '  + format(spec, '.2f'))

tp = tot_tp/3
fp = tot_fp/3 
tn= tot_tn/3
fn = tot_fn/3
accy = tot_accy/3
err = tot_err/3
sens = tot_sens/3
spec = tot_spec/3

pfp = fp / (fp + tp)
pfn = fn / (fn + tn)

print("\n\nDecision Tree Classifier Average Results:")
print('TP: ' + format(tp, '.0f'))
print('FP: '  + format(fp, '.0f'))
print('TN: '  + format(tn, '.0f'))
print('FN: '  + format(fn, '.0f'))
print('PFP: '  + format(pfp, '.2f'))
print('PFN: '  + format(pfn, '.2f'))
print('Accuracy: '  + format(accy, '.2f'))
print('Error Rate: '  + format(err, '.2f'))
print('Sensitivity: '  + format(sens, '.2f'))
print('Specificity: '  + format(spec, '.2f'))
