#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#takes a dataframe of motif 
#boolean vectors and calculates 
#a phi for each motif

#decision tree
import pandas as pd

def phi(data):
    #print("call phi")
    out = open("test.csv", 'w')

    data.to_csv(out)

    columns = list(data)
    rows = list(data.index)
    total = len(rows)   #total genes
    pos = neg = tp = fp = tn = fn = phi = 0
    phis = list()

    iterc = columns
    iterc.remove("Class")
    #print(iterc)
    features = data
    # if "Phi" not in rows:
    #     zeros = [0] * len(iterc)
    #     zero = pd.DataFrame([zeros], index = ["Phi"], columns = columns)
    #     features = features.append(zero)
    # else:
    #     rows.remove("Phi")
    
    

    for c in iterc:
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
            # else:
            #     print('Error reading data.')
            #     exit(1)

        #compute phi
        if pos == 0 :
            pos = 1
        if neg == 0:
            neg = 1

        if total != 0:
            p1 = 2 * (neg/total) * (pos/total)
            p2 = abs((fn/neg)-(fp/pos))
            p3 = abs((tn/neg)-(tp/pos))
            p4 = p2 + p3
            phi = p1 * p4
        else:
            phi = 0

       # print(phi)

        #print('putting phi into table')
        #put results in featurea array
        phis.append(phi)
        features.at['Phi', c] = phi
        

        #reset features
        pos = neg = tp = fp = tn = fn = phi = 0

    dfp = pd.DataFrame([phis], index = ["Phi"], columns = columns)
    features.append(dfp)
    #print(features)
    features.to_csv(out)
    return(features)