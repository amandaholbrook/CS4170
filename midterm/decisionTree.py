#Amanda Holbrook
#CS 4170
#Ohio Unviersity

#creates a decision tree out 
#of a set of motif boolen vectors. 
#returns the tree of best motifs.

#decision tree
import pandas as pd

from computePhi import phi

def tree(data):

    ones = list()
    zeros = list()
    rows = list(data.index)
    background = 0
    foreground = 0

    rowNames = ["Motif", "Phi", "Foreground", "Background"]
    columnNames = ["Root", "LeftChild", "RightChild", "LeftLeftChild", "LeftRightChild", "RightLeftChild", "RightRightChild"]
    tree = pd.DataFrame(index = rowNames, columns = columnNames)

    #root
    data2 = phi(data)
    data2.sort_index()
    mot = (data2.idxmax(axis=1))["Phi"]
    p = (data2.max(axis=1))["Phi"]


    for r in rows:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1
    

    tree.at['Motif', 'Root'] = mot
    tree.at['Phi', 'Root'] = p
    tree.at['Foreground', 'Root'] = foreground
    tree.at['Background', 'Root'] = background

    #print(list(data.index))
    data = data.drop(mot, axis = 1)
    df1s = data.loc[["Phi"]]
    for o in ones:
        df1s = df1s.append(data.loc[[o]])
    df1s = phi(df1s)
    df0s = data.loc[["Phi"]]
    for z in zeros:
        df0s = df0s.append(data.loc[[z]])
    df0s = phi(df0s)

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #left child
    #find motif and phi
    mot = (df1s.idxmax(axis=1))["Phi"]
    p = (df1s.max(axis=1))["Phi"]
    iters = list(df1s.index)

    #find ones and zeros lists
    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    #find foreground and background for ones
    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1

    #find foreground and background for zeros  
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    #set found values
    tree.at['Motif', 'LeftChild'] = mot
    tree.at['Phi', 'LeftChild'] = p
    tree.at['Foreground', 'LeftChild'] = foreground
    tree.at['Background', 'LeftChild'] = background


    #set new dataframes
    df1s = df1s.drop(mot, axis = 1)
    df1s2 = data.loc[["Phi"]]
    for o in ones:
        df1s2 = df1s2.append(data.loc[[o]])
    df1s2 = phi(df1s2)
    df0s2 = data.loc[["Phi"]]
    for z in zeros:
        df0s2 = df0s2.append(data.loc[[z]])
    df0s2 = phi(df0s2)

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #right child
    mot = (df0s.idxmax(axis=1))["Phi"]
    p = (df0s.max(axis=1))["Phi"]
    #print(mot)
    iters = list(df0s.index)

    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    tree.at['Motif', 'RightChild'] = mot
    tree.at['Phi', 'RightChild'] = p
    tree.at['Foreground', 'RightChild'] = foreground
    tree.at['Background', 'RightChild'] = background

    df0s = df0s.drop(mot, axis = 1)
    df1s3 = data.loc[["Phi"]]
    for o in ones:
        df1s3 = df1s3.append(data.loc[[o]])
    df1s3 = phi(df1s3)
    df0s3 = data.loc[["Phi"]]
    for z in zeros:
        df0s3 = df0s3.append(data.loc[[z]])
    df0s3 = phi(df0s3)

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #left left child
    mot = (df1s2.idxmax(axis=1))["Phi"]
    p = (df1s2.max(axis=1))["Phi"]
    #print(mot)
    iters = list(df1s2.index)

    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    tree.at['Motif', 'LeftLeftChild'] = mot
    tree.at['Phi', 'LeftLeftChild'] = p
    tree.at['Foreground', 'LeftLeftChild'] = foreground
    tree.at['Background', 'LeftLeftChild'] = background

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #left right child
    mot = (df0s2.idxmax(axis=1))["Phi"]
    p = (df0s2.max(axis=1))["Phi"]
    #print(mot)
    iters = list(df0s2.index)

    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    tree.at['Motif', 'LeftRightChild'] = mot
    tree.at['Phi', 'LeftRightChild'] = p
    tree.at['Foreground', 'LeftRightChild'] = foreground
    tree.at['Background', 'LeftRightChild'] = background

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #right left child
    mot = (df1s3.idxmax(axis=1))["Phi"]
    p = (df1s3.max(axis=1))["Phi"]
    #print(mot)
    iters = list(df1s3.index)

    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    tree.at['Motif', 'RightLeftChild'] = mot
    tree.at['Phi', 'RightLeftChild'] = p
    tree.at['Foreground', 'RightLeftChild'] = foreground
    tree.at['Background', 'RightLeftChild'] = background

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0

    #right right child
    mot = ((df0s3.idxmax(axis=1))["Phi"])
    p = (df0s3.max(axis=1))["Phi"]
    iters = list(df0s3.index)

    for r in iters:
        if data.at[r, mot] == 1:
            ones.append(r)
        elif data.at[r, mot] == 0:
            zeros.append(r)

    for o in ones:
        if data.at[o, "Class"] == 1:
            foreground += 1
        elif data.at[o, "Class"] == -1:
            background +=1
        
    for z in zeros:
        if data.at[z, "Class"] == 1:
            foreground += 1
        elif data.at[z, "Class"] == -1:
            background +=1

    tree.at['Motif', 'RightRightChild'] = mot
    tree.at['Phi', 'RightRightChild'] = p
    tree.at['Foreground', 'RightRightChild'] = foreground
    tree.at['Background', 'RightRightChild'] = background

    ones.clear()
    zeros.clear()
    background = 0
    foreground = 0



    # #print(root)
    #tree.to_csv(out)
    return tree




