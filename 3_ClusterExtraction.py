# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:39:02 2020

@author: lakki
"""

import pandas as pd
import numpy as np
import os
inflation = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
iteration = [25]


def get_files():
    graph_dir = "./iaEnronOutput/iaEnron_Inflation/"
    final_result_df = None
    result_file_path = './ExtractedClusters.csv'
    cntr = 1
    IdxSeries = []
    for infl in inflation:
        for itera in iteration:
            graph_signature_path = graph_dir + "iaEnron_Inflation_" + str(infl) + "_" + str(itera) + ".csv"
            input_df = read_file(graph_signature_path)
            final_clusters = get_clusters(input_df)
            result_df = generate_result_df(final_clusters, infl, itera)
            Len = len(final_clusters)
            for i in range(0, Len):
                IdxSeries.append("C" + str(cntr))
                cntr = cntr + 1
            IdxSeries.append("")
            if final_result_df is None:
                final_result_df = result_df
            else:
                final_result_df = final_result_df.append(result_df, ignore_index = True)
            #print("--------------------------------------------------\n\n")
    temp = pd.DataFrame(IdxSeries, columns = ['MClusterIndex'])
    cols = list(final_result_df.columns)
    cols.append('MClusterIndex')
    
    final_result_df = pd.concat([final_result_df,temp], axis = 1)
    print(final_result_df.head())
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
        
    final_result_df.to_csv(result_file_path, index = None)
    
        
def read_file(file_path):
    input_df = pd.read_csv(file_path, header = None)
    input_df = input_df.iloc[:, 0: len(input_df.columns) - 1]
    return input_df
    #get_clusters(input_df, infl, itera)
    
def get_clusters(df):
    final_clusters = set([])
    row_cluster = []
    
    nodePrefix = 'Node '
    for index, row in df.iterrows():
        row_cluster = get_non_zero_elements(row, nodePrefix)
        if bool(row_cluster):
            final_clusters.add(tuple(row_cluster))
    return final_clusters
    
def generate_result_df(final_clusters, inflation, iteration):
    #no inflation graph signature path
    graph_signature_path =  "./iaEnronOutput/iaEnron_NoInflation/iaEnron_NoInflation_1.0_" + str(iteration) + ".csv"
    
    no_inflation_df = read_file(graph_signature_path)
    
    result_dict = {'Cluster_Index' : [],
                 'Node_Ids' : [],
                 'NoInflation_Value': [],
                 'SumOfNoInflationValues' : [],
                 'NumberOfNodes' : [],
                 'Inflation': [],
                 'Iteration' : [],
                 'GraphId' : []}
    cluster_index = 1
    for cluster in final_clusters:
        noInflation_values = []
        for node in cluster:
            noInflation_values.append((no_inflation_df.iloc[node - 1])[0])
        #print(noInflation_values)
        
        result_dict['Cluster_Index'].append(cluster_index)
        result_dict['Node_Ids'].append(cluster)
        result_dict['NoInflation_Value'].append(noInflation_values)
        result_dict['SumOfNoInflationValues'].append(sum(noInflation_values))
        result_dict['NumberOfNodes'].append(len(noInflation_values))
        result_dict['Inflation'].append(inflation)
        result_dict['Iteration'].append(iteration)
        result_dict['GraphId'].append('iaEnron')
        cluster_index = cluster_index + 1
    #print(result_df)
    result_df = pd.DataFrame.from_dict(result_dict)
    result_df = result_df.append(pd.Series(), ignore_index=True)
    #print(result_df)
    return result_df
def get_non_zero_elements(row, nodePrefix):
    row_cluster = []
    for i in range(0, len(row)):
        if row[i] != 0:
            nodeLabel = i + 1#nodePrefix + 
            row_cluster.append(nodeLabel)# = row[i]
    return row_cluster
def main():
    get_files()
    
if __name__ == "__main__":
    main()
