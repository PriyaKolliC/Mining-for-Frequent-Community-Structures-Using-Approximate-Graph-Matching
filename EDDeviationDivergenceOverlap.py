import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from collections import Counter 
from more_itertools import sort_together
import collections
from operator import itemgetter 
import math
import os.path



mainGraph1 = pd.read_csv('./0_InputGraph.csv', header = None)

df = pd.read_csv('./6_Zscores' + '.csv', index_col = [0,1,2], header = [0,1,2])
df = df.iloc[:, 0:len(df)]
cols = ['']
for i in range(0, len(df)):
    cols.append(i)

deviationScores = pd.read_csv('./10_DeviationScores.csv', index_col = 0)

def common_member(a, b):
    a_set = set(a) 
    b_set = set(b) 
    
    if (a_set & b_set): 
        return (a_set & b_set) 
    else: 
        return {}

def getDscore(value, dscores):
    score = ''
    if value <= dscores[0]:
        score = '5%'
    elif value <= dscores[1]:
        score = '10%'
    elif value <= dscores[2]:
        score = '15%'
    elif value <= dscores[3]:
        score = '20%'
    elif value <= dscores[4]:
        score = '25%'
    elif value <= dscores[5]:
        score = '30%'
    elif value <= dscores[6]:
        score = '35%'
    elif value <= dscores[7]:
        score = '40%'
    elif value <= dscores[8]:
        score = '45%'
    elif value <= dscores[9]:
        score = '50%'
    else:
        score = '>50%'
    return score


def getDegrees(nodes):
    degreeDist = {}
    degreeCounts = []
    #print(nodes)
    nodes_ = [(node - 1) for node in nodes]
    #print(nodes_)
    for node in nodes_:
        degrees = mainGraph1.loc[node, :]
        degreeCount = int(sum(degrees))
        if degreeCount in degreeDist:
            degreeDist[degreeCount] = degreeDist[degreeCount] + 1
        else:
            degreeDist[degreeCount] = 1
        degreeCounts.append(degreeCount)
    degreeDist = collections.OrderedDict(sorted(degreeDist.items()))
    #print(degreeDist)
    return degreeCounts

def getCCdist(nodes):
    G = nx.from_pandas_adjacency(mainGraph1)
    CC = nx.clustering(G)
    print(CC)
    CCDist = {}
    for node in nodes:
        CCDist[node] = round(CC[node - 1], 2) 
    #print(CC)
    return CCDist
 
def checkBinData(dist1, dist2, sig1, sig2):
    flag1 = 0
    flag2 = 0
    for key in dist1.keys():
        if dist1[key] == 0:
            flag1 = 1
            break
    for key in dist2.keys():
        if dist2[key] == 0:
            flag2 = 1
            break
   
    bins = list(set(list(dist1.keys()) + list(dist2.keys())))
    
    locs = 0
    
    for bin_ in bins:
        if dist1[bin_] != 0 or dist2[bin_] != 0:
            locs += 1
           
    newLen1 = sig1
    newLen2 = sig2
    if flag1 == 1:
        nodesAdd1 = round(0.05 * sig1, 4)
        bias1 = round(nodesAdd1 / locs, 4)
        newLen1 = 0
        for key in dist1.keys():
            dist1[key] = dist1[key] + bias1
            newLen1 += dist1[key]

    if flag2 == 1:
        nodesAdd2 = round(0.05 * sig2, 4)
        bias2 = round(nodesAdd2 / locs, 4)
        newLen2 = 0
        for key in dist2.keys():
            dist2[key] = dist2[key] + bias2
            newLen2 += dist2[key]
    #print(dist1)
    #print(dist2)
    return dist1, dist2, newLen1, newLen2

def KLDivergence(dist1, dist2):
    div = 0.0
    #dist1 is Q and dist2 is P
    for key in dist1.keys():
        div += (dist1[key] * math.log(dist1[key]/dist2[key]))
        #div = div + ((dist1[key] * math.log(dist1[key]/dist2[key])) + (dist2[key] * math.log(dist2[key]/dist1[key])))/2
        #div = div + ((dist1[key] * math.log(dist1[key]/dist2[key])) + (dist2[key] * math.log(dist2[key]/dist1[key])))
        #div = div + abs(dist1[key] - dist2[key])
    #print(div)
    return div  
def getDegreeDivergence(nodes1, nodes2):
    len1 = len(nodes1)
    len2 = len(nodes2)
    
    degrees1 = getDegrees(nodes1)
    degrees2 = getDegrees(nodes2)
    #print(degrees1); print(degrees2)
    
    #----------------------binning degrees---------------------------------------
    binsStart = 0
    binsEnd = 45
    
    bins = [i for i in range(binsStart, binsEnd, 1)]
    #print(bins)
    
    
    
    indices1 = np.digitize(degrees1, bins)
    indices2 = np.digitize(degrees2, bins)
    
    g1Binned= collections.OrderedDict(sorted((dict(Counter(indices1))).items()))
    g2Binned = collections.OrderedDict(sorted((dict(Counter(indices2))).items()))
    
    #print("Originial"); print(g1Binned); print(g2Binned); print("\n")
    
    #------------------Processing bin distributions with boundaries-------------
    
    totalBins = len(bins)
    for i in range(0, totalBins):
        if i not in g1Binned:
            g1Binned[i] = 0
        if i not in g2Binned:
            g2Binned[i] = 0
    
    if len1 > len2:
        g2Binned[0] += abs(len1 - len2)
    elif len2 > len1:
        g1Binned[0] += abs(len1 - len2)
    
    g1Binned = collections.OrderedDict(sorted(g1Binned.items()))
    g2Binned = collections.OrderedDict(sorted(g2Binned.items()))
    print("Modified"); print(g1Binned); print(g2Binned); print("\n")
    #-------------------------------------KL Divergence---------------------------------
    #print("\nIn KL Divergence\n"); print("\nInput\n"); print(g1Binned); print(g2Binned)
    
    g1New, g2New, newLen1, newLen2 = checkBinData(g1Binned,g2Binned, len1, len2)
    
    
    g1BinnedDist = {}
    g2BinnedDist = {}
    
    for key in g1Binned.keys():
        g1BinnedDist[key] = round(g1New[key]/newLen1, 4)
    
    for key in g2Binned.keys():
        g2BinnedDist[key] = round(g2New[key]/newLen2, 4)
        
    divergence = KLDivergence(g1BinnedDist, g2BinnedDist)
    return divergence

def getCCDivergence(nodes1, nodes2):    
    len1 = len(nodes1)
    len2 = len(nodes2)
    
    CCs1 = list((getCCdist(nodes1)).values())
    CCs2 = list((getCCdist(nodes2)).values())
    
    #----------------------binning degrees---------------------------------------
    binsStart = 0
    binsEnd = 1.2
    
    bins = list(np.arange(binsStart, binsEnd, 0.1))
    #print(bins); print(CCs1); print(CCs2)
    
    indices1 = np.digitize(CCs1, bins)
    indices2 = np.digitize(CCs2, bins)
    
    #print(indices1, indices2)
    g1Binned= collections.OrderedDict(sorted((dict(Counter(indices1))).items()))
    g2Binned = collections.OrderedDict(sorted((dict(Counter(indices2))).items()))
    
    #print("Original"); print(g1Binned); print(g2Binned); print("\n")
    
    #------------------Processing bin distributions with boundaries-------------
    totalBins = len(bins)
    for i in range(0, totalBins):
        if i not in g1Binned:
            g1Binned[i] = 0
        if i not in g2Binned:
            g2Binned[i] = 0
    
    if len1 > len2:
        g2Binned[0] += abs(len1 - len2)
    elif len2 > len1:
        g1Binned[0] += abs(len1 - len2)
    
    g1Binned = collections.OrderedDict(sorted(g1Binned.items()))
    g2Binned = collections.OrderedDict(sorted(g2Binned.items()))
    
    #print("Modified"); print(g1Binned); print(g2Binned); print("\n")
    #-------------------------------------KL Divergence---------------------------------
    #print("\nIn KL Divergence\n"); print("\nInput\n"); print(g1Binned); print(g2Binned)
    g1New, g2New, newLen1, newLen2 = checkBinData(g1Binned,g2Binned, len1, len2)
    
    
    g1BinnedDist = {}
    g2BinnedDist = {}
    
    for key in g1Binned.keys():
        g1BinnedDist[key] = round(g1New[key]/newLen1, 4)
    
    for key in g2Binned.keys():
        g2BinnedDist[key] = round(g2New[key]/newLen2, 4)
    
    
    divergence = KLDivergence(g1BinnedDist, g2BinnedDist)
    return divergence
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def processMetrics(row, cluster1, nodes1):
    childHeader = ['']
    overlap = ['NodeOverlap']
    dScoreValdn = ['Deviation']
    Ddivergences = ['DegreeDivergence']
    ccDivergences = ['CCDivergence']
    dscores = list(deviationScores.loc[cluster1,:])
    nodes = [str(nodes1)]
    twed = [cluster1 + ": " + str(len(nodes1))]
    result_df = pd.DataFrame()
    
    sortedRow = row.sort_values()
    Index = list(sortedRow.index)
    Values = sortedRow.values
    i = 0
    
    for idx in Index:
        cluster2 = idx[0]
        
        nodes2 = idx[2]
        nodes2 = nodes2.replace('[', '')
        nodes2 = nodes2.replace(']', '')
        nodes2 = nodes2.split(",")
        nodes2 = list(map(int, nodes2)) 
        print("\n", cluster1, cluster2)
        nodes.append(str(nodes2))
        childHeader.append(cluster2 + ": " + str(len(nodes2)))
        
        if abs(len(nodes1) - len(nodes2)) <= 6:
            twed.append(str(Values[i]))
            overlap.append(str(len(common_member(nodes1, nodes2)))) 
            if cluster1 == cluster2:
                dScoreValdn.append('-')
            else:
                dScoreValdn.append(getDscore(Values[i], dscores))
                
            #Ddivergences.append(getDegreeDivergence(subGr1, subGr2, nodes1, nodes2))
            Ddivergences.append(getDegreeDivergence(nodes1, nodes2))
            ccDivergences.append(getCCDivergence(nodes1, nodes2))
        else:
            twed.append('-')
            overlap.append('-')
            dScoreValdn.append('')
            Ddivergences.append('')
            ccDivergences.append('')
        result_df[cluster2 + ": " + str(len(nodes2))] = [twed]
        i += 1
        #break
    df_ = pd.DataFrame([childHeader], columns = cols)
    df_ = df_.append(pd.Series(twed, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(dScoreValdn, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(Ddivergences, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(ccDivergences, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(nodes, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(overlap, index = cols), ignore_index = True)
    df_ = df_.append(pd.Series(), ignore_index = True)

    writeToFile(df_)
    #with open("./12_EDDevDivOverlapFeb1" + ".csv", 'a', newline = '\n') as f:
    #    df_.to_csv(f, header=False, index = None)
def writeToFile(df):
    with open("./12_EDDevDivOverlapFeb1" + ".csv", 'a', newline = '\n') as f:
        df.to_csv(f, header=False, index = None)
def removeFile():
    if os.path.exists("./12_EDDevDivOverlapFeb1" + ".csv"):
        os.remove("./12_EDDevDivOverlapFeb1" + ".csv")

removeFile()    
    
    
result_df = {}

#if os.path.exists("./12_EDDevDivOverlapFeb1" + ".csv"):
#    os.remove("./12_EDDevDivOverlapFeb1" + ".csv")


for idx1, row1 in df.iterrows():
    nodes1 = idx1[2]
    nodes1 = nodes1.replace('[', '')
    nodes1 = nodes1.replace(']', '')
    nodes1 = nodes1.split(",")
    nodes1 = list(map(int, nodes1))
    cluster1 = idx1[0]
    
    result_df = pd.DataFrame()
    dscores = list(deviationScores.loc[cluster1,:])
    i = 0
    #if cluster1 == 'C3':
    processMetrics(row1, cluster1, nodes1)
    #break