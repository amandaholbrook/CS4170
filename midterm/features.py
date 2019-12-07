#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#runs feature selection on 
#a set of motif boolean vectors


import sys, os, argparse
import pandas as pd

# #command line for giving file name
# parser = argparse.ArgumentParser()
# parser.add_argument('-f', action = "store", dest = 'input', help='the data input file')
# results = parser.parse_args()
# input = results.input #data input file

out = open('featureresults.csv', 'w')

#open file
infile = open(input, 'r')

def features(data):

    #read file into a datafram
    data = pd.read_csv(infile, index_col = 0)
    rows = list(data.index) 
    columns = list(data)
    iterc = columns
    iterc.remove("Class")

    total = len(rows)   #total genes
    pos = 0     #total positive (1) genes
    neg = 0     #total negative (0) genes
    tp = 0      #total true postives
    fp = 0      #total false postives
    tn = 0      #total true negative
    fn = 0      #total false negatives
    accy = 0    #overall accuracy
    phi = 0
    err = 0
    sens = 0
    spec = 0
    pfn = 0
    pfp = 0

    #dataframe for feature exploration
    features = pd.DataFrame(index = [iterc], columns = ['TP', 'FP', 'TN', 'FN', 'Accuracy', 'Error Rate', 'Sensitivity', 'Specificity', 'Phi'])

    count = 1
    #iterate through data
    for c in iterc:
        print('feature ' + str(count) + '/' + str(len(iterc)))
        for r in rows:
            if data.at[r, c] == 1:
                #true postive = contains gene & class of 1
                if data.at[r, 'Class'] == 1:
                    tp += 1
                    pos += 1
                #false postive = contains gene & class of -1
                elif data.at[r, 'Class'] == -1:
                    fp += 1
                    pos += 1
            elif data.at[r, c] == 0:
                #false negative = doesn't contain gene & class of 1
                if data.at[r, 'Class'] == 1:
                    fn += 1
                    neg += 1
                #true negative = doesn't contain gene & class of -1
                elif data.at[r, 'Class'] == -1:
                    tn += 1
                    neg += 1
            else:
                print('Error reading data.')
                exit(1)

        #compute accuracy (TN + TP) / (TN + FN + FP + TP)
        accy = (tn + tp) / (tn + fn + fp + tp)

        #compute phi
        if pos == 0 :
            pos = 1
        if neg == 0:
            neg = 1

        p1 = 2 * (neg/total) * (pos/total)
        p2 = abs((fn/neg)-(fp/pos))
        p3 = abs((tn/neg)-(tp/pos))
        p4 = p2 + p3
        phi = p1 * p4

        err = (fn + fp) / (tn + fn + fp + tp)
        pfp = fp / (fp + tp)
        pfn = fn / (fn + tn)
        sens = tp / (tp + fn)
        spec = tn = (fp + tn)

        print('putting features into table')
        #put results in featurea array
        features.at[c, 'TP'] = tp
        features.at[c, 'FP'] = fp
        features.at[c, 'TN'] = tn
        features.at[c, 'FN'] = fn
        features.at[c, 'Accuracy'] = accy
        features.at[c, 'Phi'] = phi
        features.at[c, 'Error Rate'] = err
        features.at[c, 'Sensitivity'] = sens
        features.at[c, 'Specificity'] = spec
        features.at[c, 'PFP'] = pfp
        features.at[c, 'PFN'] = pfn

        #reset features
        pos = 0
        neg = 0
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        accy = 0
        phi = 0
        err = 0
        sens = 0
        spec = 0
        pfn = 0
        pfp = 0

        count += 1

    features = features.sort_values(by = ["Phi"], ascending = False)
    return features
    #features.to_csv(out)