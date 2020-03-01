import pandas as pd
import constants
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(constants.RAW_DATA_PATH + '/../raw_data.csv')

datasets = list(set(df['dataset'].values.tolist()))
classes = list(set(df['class'].values.tolist()))

N = len(classes)
ind = np.arange(N)    # the x locations for the groups
width = 0.5     # the width of the bars: can also be len(x) sequence

plt.rcParams.update({'font.size': 25})

nbs_oxford = []  
for doggo_class in classes:
    new_df = df[(df['class']==doggo_class)&(df['dataset']=='oxford')]
    nb = new_df.shape[0]
    nbs_oxford.append(nb)

p1 = plt.bar(ind, nbs_oxford, width)

nbs_stanford = []  
for doggo_class in classes:
    new_df = df[(df['class']==doggo_class)&(df['dataset']=='stanford')]
    nb = new_df.shape[0]
    nbs_stanford.append(nb)

p2 = plt.bar(ind, nbs_stanford, width, bottom=nbs_oxford)      
    
nbs_udacity = []  
for doggo_class in classes:
    new_df = df[(df['class']==doggo_class)&(df['dataset']=='udacity')]
    nb = new_df.shape[0]
    nbs_udacity.append(nb)

p3 = plt.bar(ind, nbs_udacity, width, bottom=[nbs_stanford[i] + nbs_oxford[i] for i in range(len(classes))])  



plt.xticks(ind, classes)
plt.yticks(np.arange(0, 2000, 500))
plt.legend((p1[0], p2[0], p3[0]), ['oxford', 'stanford', 'udacity'])

plt.show()