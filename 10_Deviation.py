# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:19:10 2021

@author: lakki
"""

import pandas as pd
import numpy as np

df = pd.read_csv("../PythonOutput/4_UniqueClusters.csv", header = 0)
deviations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

deviatedScores = {}
for idx, row in df.iterrows():
    clusterId = row['Cluster_Index']
    signature = row['NoInflation_Value']
    signature = signature.replace('[', '')
    signature = signature.replace(']', '')
    signature = signature.split(', ')
    signature = list(map(float, signature))
    signature = [float(i)/sum(signature) for i in signature]
    #print(signature)
    
    if clusterId not in deviatedScores.keys():
        deviatedScores[clusterId] = []
    for deviation in deviations:
        deviated = [((deviation/100) * val) for val in signature]
        score = 0
        for i in range(0, len(signature)):
            score = score + pow(deviated[i], 2)
        #print(score)
        deviatedScores[clusterId].append(score)
        
    #break
deviatedScores = pd.DataFrame.from_dict(deviatedScores, orient = 'index')
deviatedScores.columns = ['5% deviation', '10% deviation', '15% deviation',
                          '20% deviation', '25% deviation', '30% deviation',
                          '35% deviation', '40% deviation', '45% deviation',
                          '50% deviation']
deviatedScores.to_csv('../PythonOutput/10_DeviationScores.csv')
print(deviatedScores)
