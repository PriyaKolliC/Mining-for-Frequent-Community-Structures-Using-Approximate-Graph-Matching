# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:12:08 2020

@author: lakki
"""
import pandas as pd
import numpy as np
data = pd.read_csv('A:/University of Cincinnati/theses/newDatasets/ia-enron.csv', header = None)


#data_list = np.empty(shape = (143,143), dtype = int)
w, h = 143,143
data_list = [[0 for x in range(w)] for y in range(h)] 
#print(data_list)

for idx,row in data.iterrows():
    node1, node2 = row[0].split(' ')
    print(node1, node2)
    node1 = int(node1) - 1
    node2 = int(node2) - 1
    data_list[node1][node2] = 1
    data_list[node2][node1] = 1
print(data_list)  
df = pd.DataFrame(data_list)
print(df)
df.to_csv('ia-enronGraph.csv', header = None, index = None)
