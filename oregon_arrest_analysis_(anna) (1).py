# -*- coding: utf-8 -*-
"""OREGON Arrest Analysis (anna).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kchDTfhL69aAuNMBJmlfIrSrP8j7bBrJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from math import pi

from google.colab import files
uploaded = files.upload()

data_path = "oregonfinalversion1.csv"
arrests = pd.read_csv(data_path, index_col=0)
#arrests.loc[' STATEWIDE TOTAL']
arrests.head()





race = ['White', 'Black', 'Other']
totalArrests = [83117, 3307, 10470]

fig, ax=plt.subplots(figsize = (5,5)) ##creating bar chart
plt.bar(race, totalArrests)
plt.xlabel('Race')
plt.ylabel('Total Arrests')
plt.title('Total Arrests in Oregon in 2019 by Race')
for i, data in enumerate(totalArrests): ##adding labels to bars
  plt.text(x=i, y=data+1, s=f"{data}", ha='center') 
plt.show()

r = ['White', 'Black', 'Other']
rawData = {'greenBars':[83117, 3307,10470], 'blueBars':[3163765,92680,956292]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

plt.xticks(r, names)
plt.xlabel("Race")
plt.ylabel("Percentage")
plt.ylim(0,30)

plt.title('Arrests as % of Population in Oregon')
plt.show()

r2 = ['White', 'Black','Other']
rawData = {'greenBars':[10979,1335,2522], 'blueBars':[83117,3307,10470]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r2, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r2, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

plt.xticks(r2)
plt.ylim(0,30)
plt.xlabel("Race")
plt.ylabel("Percentage")

plt.title('Prison population as a proportion of arrests in Oregon')
plt.show()

from google.colab import files
uploaded = files.upload()

data_path = "Oregonarrestoffencetypeanna.csv"
arrests = pd.read_csv(data_path, index_col=0)
#arrests.loc[' STATEWIDE TOTAL']
print(arrests)

import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = arrests.iloc[0:3]
print(df)
 

N=3


# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], df.index)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([20000,40000,60000], ["20000","40000","60000"], color="grey", size=7)
plt.ylim(0,60000)
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=list(df["White"].values)
values += values[:1]
print(values)
ax.plot(angles, values, linewidth=1, linestyle='solid', label="White")
ax.fill(angles, values, 'b', alpha=0.1)
 
values=list(df["Black"].values)
values += values[:1]
print(values)
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Black")
ax.fill(angles, values, 'r', alpha=0.1)

values=list(df["Hispanic"].values)
values += values[:1]
print(values)
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Hispanic")
ax.fill(angles, values, 'g', alpha=0.1)
# Ind2
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))