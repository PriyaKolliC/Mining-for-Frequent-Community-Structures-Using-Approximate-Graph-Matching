import matlab.engine
import pandas as pd
import sys
import numpy as np
eng = matlab.engine.start_matlab()

penalty = 2
def cumulative_edr(ans):
    print(ans)
    g1_visited = set()
    g2_visited = set()
    cumulative_sum = 0
    
    for idx, row in ans.iterrows():
        s1 = row['Signal1']
        s2 = row['Signal2']
        ed = row['ED']
        cumulative_sum = cumulative_sum + ed
        '''
        if s1 not in g1_visited and s2 not in g2_visited:
            cumulative_sum = cumulative_sum + ed
        else:
            cumulative_sum = cumulative_sum + penalty * ed
        g1_visited.add(s1)
        g2_visited.add(s2)
        ''' 
    return cumulative_sum
    
    
         
file_path = "../PythonOutput/4_UniqueClusters.csv";
input_data = pd.read_csv(file_path);
input_data.dropna(inplace=True);
#print(input_data)

cnt = 0;
result_dict = {}
row_inflation = input_data['Inflation']
col_inflation = input_data['Inflation']
min_nodes = 3
max_nodes = 20
one = []
two = []
three = []
one_ = []
two_ = []
three_ = []
for idx1, row1 in input_data.iterrows():               
    nodeID_c1 = row1['Node_Ids'];
    cluster1 = row1['NoInflation_Value'];
    
    cluster1 = cluster1.replace('[', '');
    cluster1 = cluster1.replace(']', '');
    cluster1 = cluster1.split(",");
    cluster1 = list(map(float, cluster1));
    
    nodeID_c1 = nodeID_c1.replace('(', '');
    nodeID_c1 = nodeID_c1.replace(')', '');
    nodeID_c1 = nodeID_c1.split(",");
    nodeID_c1 = list(filter(None, nodeID_c1))
    nodeID1 = list(map(int, nodeID_c1));
  
    clusterID1 = row1['Cluster_Index']
    row_index =  clusterID1
    #if len(nodeID1) < 3 or len(nodeID1)> 20:
    #    continue
    
    for idx2, row2 in input_data.iterrows():
        clusterID2 = row2['Cluster_Index']
        #print(clusterID1, clusterID2)
        
        nodeID_c2 = row2['Node_Ids'];
        nodeID_c2 = nodeID_c2.replace('(', '');
        nodeID_c2 = nodeID_c2.replace(')', '');
        
        nodeID_c2 = nodeID_c2.split(",");
        nodeID_c2 = list(filter(None, nodeID_c2))         
        nodeID2 = list(map(int, nodeID_c2));
        #if len(nodeID2) < 3 or len(nodeID2)> 20:
        #    continue
        col_index = clusterID2
            
        cluster2 = row2['NoInflation_Value'];    
        cluster2 = cluster2.replace('[', '');
        cluster2 = cluster2.replace(']', '');
        cluster2 = cluster2.split(",");
        
        cluster2 = list(map(float, cluster2));
        if (row_index in result_dict and col_index in result_dict[row_index]) or (col_index in result_dict and row_index in result_dict[col_index]):
            continue
        
        ans, dist = eng.edr_clusters(matlab.double(cluster1), matlab.double(cluster2), matlab.double(nodeID1), matlab.double(nodeID2), nargout = 2);
        ans = pd.DataFrame(np.array(ans));
        ans.columns = ['Signal1', 'Signal2', 'NodeID1', 'NodeID2', 'Val1', 'Val2', 'ED'];
        cumulative_sum = cumulative_edr(ans);  
        
        if row_index not in result_dict:
            result_dict[row_index] = {col_index : cumulative_sum}
        else:
            result_dict[row_index][col_index] = cumulative_sum
        if col_index not in result_dict:
            result_dict[col_index] = {row_index : cumulative_sum}
        else:
            result_dict[col_index][row_index] = cumulative_sum
        
result_df = pd.DataFrame.from_dict(result_dict, orient = 'index')
#print(result_df.shape)
#print(result_df.head())

clusters = list(result_df.columns)
inflations = []
temp = input_data.loc[input_data['Cluster_Index'].isin(clusters)]
    
inflations = list(temp["Inflation"])
nodeIds = list(temp["Node_Ids"])
#print(clusters)
#print(inflations)
#print(nodeIds)
clusters = pd.Series(clusters)
inflations = pd.Series(inflations)
nodeIds = pd.Series(nodeIds)
row_index = pd.concat([clusters, inflations, nodeIds], axis = 1)
col_headers = [clusters, inflations, nodeIds]
result_df.columns = col_headers
result_df.index = [clusters, inflations, nodeIds]
result_df.to_csv('../PythonOutput/5_CumulativeSum' + '.csv')
