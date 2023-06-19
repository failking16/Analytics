# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:27:57 2023

@author: jksls
"""

import pandas as pd
import numpy as np

#Variables for the analysis from the our dataset
df      = pd.read_csv('set/dataset.csv')
bas_exp = np.array(df['bas.exp'])
ad_exp  = np.array(df['ad.exp'])
player  = np.array(df['Player'])
year    = np.array(df['Year'])
from_cl = np.array(df['From Club'])
to_club = np.array(df['To Club'])

import matplotlib.pyplot as mpl
mpl.style.use('fivethirtyeight')

def generate_colors(n):
    cmap   = mpl.get_cmap('tab10')
    colors = [cmap(i) for i in np.linspace(0, 1, n)]
    return colors

un_names, counts = np.unique(df['Player'],return_counts = True)
scat_val         = []

for i in range(len(un_names)):
    if counts[i] > 1 :
        scat_val.append(i)

scatter_x = un_names[scat_val]
scatter_y = counts[scat_val]
colors    = generate_colors(len(scatter_x))

cum_sum = np.zeros(len(scatter_x))
for i in range(len(scatter_x)):
    fee_sum = 0
    for j in range(len(bas_exp)):
        if player[j] == scatter_x[i]:
            fee_sum += int(bas_exp[j]) + int(ad_exp[j])
    cum_sum[i] = fee_sum

mpl.scatter(scatter_x,scatter_y,color = colors)
for i, text in enumerate(cum_sum):
    mpl.text(scatter_x[i],scatter_y[i],str(text))
mpl.xticks(range(len(scatter_x)),[x[:6] for x in scatter_x])
mpl.yticks(np.arange(0,max(counts)+2,1))
mpl.show()

un_ye, counts = np.unique(np.sort(year), return_counts=True)
cum_sum       = np.zeros(len(un_ye))
labels        = [str(year) for year in un_ye]

for i in range(len(un_ye)):
    fee_sum = 0
    for j in range(len(year)):
        if year[j] == un_ye[i]:
            fee_sum += int(bas_exp[j]) + int(ad_exp[j])
    cum_sum[i] = fee_sum

mpl.bar(un_ye, counts, color=generate_colors(len(un_ye)), width=0.7)
mpl.xticks(un_ye, labels, rotation='vertical')
mpl.yticks(np.arange(0, max(counts) + 3, 1))
for i, text in enumerate(cum_sum):
    mpl.text(un_ye[i], counts[i], str(text),rotation= 'vertical',ha='center', va='bottom')

mpl.subplots_adjust(bottom=0.3)
mpl.tight_layout()
mpl.show()

un_fc, count = np.unique(np.sort(from_cl),return_counts=True)
copy_count   = count.copy()
lar_ind      = []

for i in range(5):
    for j in range(len(count)):
        if copy_count[j] == max(copy_count):
            lar_ind.append(j)
            copy_count[j] = 0
            break
        
un_fc   = un_fc[lar_ind]
count   = count[lar_ind]
cum_sum = np.zeros(len(un_fc))

for i in range(len(un_fc)):
    fee_sum = 0
    for j in range(len(from_cl)):
        if from_cl[j] == un_fc[i]:
            fee_sum += int(bas_exp[j]) + int(ad_exp[j])
    cum_sum[i] = fee_sum

labels = [f'{un_cl}\n${cum_sum}' for un_cl, cum_sum in zip(un_fc, cum_sum)]
mpl.pie(count,labels = labels, autopct='%1.1f%%', colors = generate_colors(len(un_fc))) 
mpl.axis('equal')
mpl.show()

un_fc, count = np.unique(np.sort(to_club),return_counts=True)
copy_count   = count.copy()
lar_ind      = []

for i in range(5):
    for j in range(len(count)):
        if copy_count[j] == max(copy_count):
            lar_ind.append(j)
            copy_count[j] = 0
            break
        
un_fc   = un_fc[lar_ind]
count   = count[lar_ind]
cum_sum = np.zeros(len(un_fc))

for i in range(len(un_fc)):
    fee_sum = 0
    for j in range(len(from_cl)):
        if to_club[j] == un_fc[i]:
            fee_sum += int(bas_exp[j]) + int(ad_exp[j])
    cum_sum[i] = fee_sum

labels = [f'{un_cl}\n${cum_sum}' for un_cl, cum_sum in zip(un_fc, cum_sum)]
mpl.pie(count,labels = labels, autopct='%1.1f%%', colors = generate_colors(len(un_fc))) 
mpl.axis('equal')
mpl.show()

un_fc = np.unique(np.sort(to_club))
cum_sum = np.zeros(len(un_fc))
labels  = [str(un_fc) for un_fc in un_fc]
for i in range(len(un_fc)):
    tt_fee = 0
    for j in range(len(to_club)):
        if to_club[j] == un_fc[i]:
            tt_fee -= (int(bas_exp[j]) + int(ad_exp[j]))
        if from_cl[j] == un_fc[i]:
            tt_fee += int(bas_exp[j]) + int(ad_exp[j])
    cum_sum[i] = tt_fee

mpl.bar(un_fc, cum_sum, color=generate_colors(len(un_fc)), width=0.7)
mpl.xticks(un_fc, labels, rotation='vertical')
mpl.yticks(np.arange(min(cum_sum) - 250, max(cum_sum) + 250 , 250))
mpl.subplots_adjust(bottom=0.3)
mpl.tight_layout()
mpl.show()


# This part of the code can be used for visualisation of cumulative sum if there are some positive numebr, but in
# this case we have cum_sum only negative numbers

# names    = [ind for ind in range(len(un_fc)) if cum_sum[ind] > 0]
# un_fcp   = un_fc[names]
# un_fcn   = un_fc[[ind for ind in range(len(un_fc)) if cum_sum[ind] < 0]]
# cum_sump = cum_sum[names]
# cum_sumn = abs(cum_sum[[ind for ind in range(len(un_fc)) if cum_sum[ind] < 0]])
# labelsp  = [str(year) for year in un_fcp]
# labelsn  = [str(year) for year in un_fcn]

# mpl.bar(un_fcp, cum_sump, color=generate_colors(len(un_fcp)), width=0.7)
# mpl.xticks(un_fcp, labelsp, rotation='vertical')
# mpl.yticks(np.arange(np.nanmin(cum_sump), np.nanmax(cum_sump) + 250, 250))
# mpl.subplots_adjust(bottom=0.3)
# mpl.tight_layout()
# mpl.show()

# mpl.bar(un_fcn, cum_sumn, color=generate_colors(len(un_fcn)), width=0.7)
# mpl.xticks(un_fcn, labelsn, rotation='vertical')
# mpl.yticks(np.arange(np.nanmin(cum_sumn), np.nanmax(cum_sumn) + 250, 250))
# mpl.subplots_adjust(bottom=0.3)
# mpl.tight_layout()
# mpl.show()

