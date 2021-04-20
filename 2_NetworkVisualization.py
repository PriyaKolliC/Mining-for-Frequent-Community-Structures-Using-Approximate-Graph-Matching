# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:34:15 2020

@author: lakki
"""

import pandas as pd
import networkx as nx
from matplotlib.pyplot import figure

df = pd.read_csv('ia-enron.csv', header = None)
edge_list = []

for idx, row in df.iterrows():
    node1 = int(row[0])
    node2 = int(row[1])
    edge_list.append([node1, node2])


G = nx.DiGraph()
G = nx.from_edgelist(edge_list)
figure(figsize=(40, 40))
nx.draw_networkx(G, with_labels = True)
    
'''
    node1, node2 = row[0].split()
    edge_list.append([int(node1), int(node2)])
    #print(node1, node2)
    #break
#print(edge_list)
G = nx.DiGraph()
G = nx.from_edgelist(edge_list)
print(G)

#nx.draw_shell(G, with_labels=True)

print(df)


#G = nx.from_edgelist(df)
G = nx.adjacency_matrix(df)
#G = nx.from_pandas_edgelist(df)
'''