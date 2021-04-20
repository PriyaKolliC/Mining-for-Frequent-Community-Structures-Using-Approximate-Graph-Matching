import pandas as pd

penalty = 2
def calculateZScores(row):
    #row = row.replace('-', '0')
    row = pd.to_numeric(row)
    mean = row.mean()
    std = row.std()
    z_scores_row = []
    for item in row:
        z_scores_row.append((item - mean)/std)
    return z_scores_row
    

file_path = "../PythonOutput/5_CumulativeSum" + ".csv";
input_data = pd.read_csv(file_path, header=[0,1,2], index_col = [0,1,2], skipinitialspace=True);
#print(input_data.head())
Zero_df = []
nonZero_df = []
z_scores_df = []
for idx, row in input_data.iterrows():
    zero_values = []
    nonZero_values = []
    z_scores = []
    z_scores_row = calculateZScores(row)
    sorted_row = row.sort_values()
    #print(row.index)
    #print(sorted_row.values)
    #print(sorted_row.index)
    for i in range(0, len(sorted_row)):
        if len(zero_values) == 2 and len(nonZero_values) == 2:
            break
        try:
            if float(sorted_row[i]) == 0.0:
                if len(zero_values) < 2:
                    zero_values.append(sorted_row.index[i][0])
            else:
                if len(nonZero_values) < 2:
                    nonZero_values.append(sorted_row.index[i][0])
                    z_scores.append(round(z_scores_row[i], 2))
                    
        except:
            temp = ""
    Zero_df.append(str(zero_values))
    nonZero_df.append(str(nonZero_values))
    z_scores_df.append(str(z_scores))

zero_df = pd.DataFrame(Zero_df)
#zero_df.index = input_data.index

nonzero_df = pd.DataFrame(nonZero_df)
#nonzero_df.index = input_data.index

z_scores_df = pd.DataFrame(z_scores_df)
#z_scores_df.index = input_data.index

result_df = pd.concat([zero_df, nonzero_df], axis = 1)
result_df = pd.concat([result_df, z_scores_df], axis = 1)
#print(result_df.head())
one = pd.Series(['', '', ''])
two = pd.Series(['', '', ''])
three = pd.Series(['', '', ''])
four = pd.Series(['ZeroSum_Clusters','NonZeroSum_Clusters', 'Z-Scores'])

#print(result_df.head())
result_df.columns = [one,two,four]
#print(result_df.head())
result_df.index = input_data.index
final_df = pd.concat([input_data, result_df], axis = 1)
#print(final_df.head())
final_df.to_csv('../PythonOutput/6_Zscores' + '.csv')
