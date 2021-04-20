# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:07:49 2021

@author: lakki
"""

import pandas as pd
import numpy as np
import os.path


penalty = 2
def common_member(a, b):
    a_set = set(a) 
    b_set = set(b) 
    
    if (a_set & b_set): 
        return (a_set & b_set) 
    else: 
        return {}

df = pd.read_csv('../PythonOutput/6_Zscores' + '.csv', index_col = [0,1,2], header = [0,1,2])
#print(df.head())
df = df.iloc[:, 0:len(df)]


deviationScores = pd.read_csv('../PythonOutput/10_DeviationScores.csv', index_col = 0)
#print(deviationScores)

#clustersOfInterest = ['C3', ]
#df = df.iloc[:, -398]
#df = df.iloc[:, -397]
result_df = {}
cols = ['']
for i in range(0, len(df)):
    cols.append(i)

if os.path.exists("../PythonOutput/11_DeviationsOverlapNodes" + ".csv"):
    os.remove("../PythonOutput/11_DeviationsOverlapNodes" + ".csv")
#print(cols)
for idx1, row1 in df.iterrows():
    nodes1 = idx1[2]
    nodes1 = nodes1.replace('(', '')
    nodes1 = nodes1.replace(')', '')
    nodes1 = nodes1.split(",")
    nodes1 = list(filter(None, nodes1))
    nodes1 = list(map(int, nodes1))
    #print(list(row1))
    sortedRow = row1.sort_values()
    Index = list(sortedRow.index)
    Values = sortedRow.values
    
    result = ['']
    twed = [idx1[0] + ": " + str(len(nodes1))]
    overlap = ['NodeOverlap']
    i = 0
    result_df = pd.DataFrame()
    dscores = list(deviationScores.loc[idx1[0],:])
    #print(dscores)
    #break
    dScoreValdn = ['Deviation']
    for idx2 in Index:
        nodes2 = idx2[2]
        nodes2 = nodes2.replace('(', '');
        nodes2 = nodes2.replace(')', '');
        nodes2 = nodes2.split(",");
        nodes2 = list(filter(None, nodes2))
        nodes2 = list(map(int, nodes2));    
        resStr = idx2[0]  + ": " + str(len(nodes2))
        result.append(resStr)        
        if abs(len(nodes1) - len(nodes2)) <= 6:
            twed.append(str(Values[i]))
            overlap.append(str(len(common_member(nodes1, nodes2)))) 
            if idx1[0] == idx2[0]:
                dScoreValdn.append('-')
            elif Values[i] <= dscores[0]:
                dScoreValdn.append('5%')
            elif Values[i] <= dscores[1]:
                dScoreValdn.append('10%')
            elif Values[i] <= dscores[2]:
                dScoreValdn.append('15%')
            elif Values[i] <= dscores[3]:
                dScoreValdn.append('20%')
            elif Values[i] <= dscores[4]:
                dScoreValdn.append('25%')
            elif Values[i] <= dscores[5]:
                dScoreValdn.append('30%')
            elif Values[i] <= dscores[6]:
                dScoreValdn.append('35%')
            elif Values[i] <= dscores[7]:
                dScoreValdn.append('40%')
            elif Values[i] <= dscores[8]:
                dScoreValdn.append('45%')
            elif Values[i] <= dscores[9]:
                dScoreValdn.append('50%')
            else:
                dScoreValdn.append('>50%')
        else:
            twed.append('-')
            overlap.append('-')
            dScoreValdn.append('')
        result_df[resStr] = [twed]
        i += 1
    df_ = pd.DataFrame([result], columns = cols)
    df_ = df_.append(pd.Series(twed, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(dScoreValdn, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(overlap, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(), ignore_index = True)


    with open("../PythonOutput/11_DeviationsOverlapNodes" + ".csv", 'a', newline = '\n') as f:
        df_.to_csv(f, header=False, index = None)
    
    #break

    


    