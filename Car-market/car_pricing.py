# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:30:55 2023

@author: jksls
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as mpl
mpl.style.use('fivethirtyeight')

df = pd.read_csv('dataset/new_cars_prices.csv')
df.dropna(axis=0 , how='any' , inplace = True)

p_old    = np.array(df['Old Price'], dtype=str)
p_new    = np.array(df['New Price'], dtype=str)
p_old    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '') for k in p_old])
p_new    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '') for k in p_new])
p_old    = p_old.astype(int)
p_new    = p_new.astype(int)
name     = np.array(df['Car Model'])
date     = np.array(df['date_range'])
diff     = np.array([(p_new[i] - p_old[i]) for i in range(len(p_old))])
diff_abs = np.array([abs(diff[i]) for i in range(len(diff))])
uniq_nam = np.unique(name)


# Max of old and new prices and the name of the car
print(max(p_old),max(p_new))
print(name[p_old == max(p_old)] , name[p_new == max(p_new)])

# Min of old and new prices and the name of the car
print(min(p_old) , min(p_new))
print(name[p_old == min(p_old)] , name[p_new == min(p_new)])

p_avg       = []
dif_avg     = []
dif_avg_abs = []

for i in range(len(uniq_nam)):
    merged_p = np.unique(np.concatenate([p_old[name == uniq_nam[i]],p_new[name == uniq_nam[i]]]))
    p_avg.append(merged_p.mean())
    dif_avg.append(diff[name == uniq_nam[i]].mean())
    dif_avg_abs.append(diff_abs.mean())    

print(max(p_avg) , max(dif_avg) , max(dif_avg_abs))
print(min(p_avg) , min(dif_avg) , min(dif_avg_abs))

print()
