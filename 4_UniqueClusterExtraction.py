import pandas as pd

file_path = './ExtractedClusters.csv'
input_data = pd.read_csv(file_path)
input_data.dropna(inplace=True);

data = {}
i = 1
cluster_set = set([])
for idx, row in input_data.iterrows():
    key = row['Node_Ids']
    #print(key)
    if key not in data.keys():
        data[key] = {'Cluster_Index' :  'C' + str(i),
                    'Node_ids' : row['Node_Ids'],
                    'NoInflation_Value' : row['NoInflation_Value'],
                    'SumOfNoInflationValues' : row['SumOfNoInflationValues'],
                    'NumberOfNodes' : row['NumberOfNodes'],
                    'Inflation' : [row['Inflation']],
                    'Iteration' : [row['Iteration']]}
        i = i + 1
    else:
        #print(data)
        data[key]['Inflation'].append(row['Inflation'])
        #data[key]['Iteration'].append(row['Iteration'])
        
data = pd.DataFrame(data.values())
data.to_csv('./UniqueClusters.csv', index = None)
print(data)
