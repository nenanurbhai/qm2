# -*- coding: utf-8 -*-
"""UK and Wales code .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bnsi3pleXC-ZmnxPUqvgWQa27ucZ-E_J
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from math import pi

from google.colab import files
uploaded = files.upload()

data_path = "arrestsuk2.0.csv"
arrests = pd.read_csv(data_path, index_col=0)
arrests.head()

arrests2 = arrests.drop(arrests.columns[[0]], axis=1)

arrests2.head()

arrests3 = arrests2.drop(labels=['Indian', 'Pakistani', 'Asian other', 'Black African', 'Black Caribbean', 'Black other', 'Mixed White/Asian', 'Mixed White/Black African', 'Mixed White/Black Caribbean', 'Mixed other', 'White British', 'White Irish', 'White other'])
arrests3.head()

transposedArrests = np.transpose(arrests3)
cleanArrests = transposedArrests.replace(',', '', regex=True) ##REGEX is a way of replacing and cleaning text
cleanArrests.head()

cleanArrests[["Asian", "Chinese", 'Other inc Chinese']] = cleanArrests[["Asian", "Chinese", 'Other inc Chinese']].apply(pd.to_numeric)

sum_column = cleanArrests["Asian"] + cleanArrests["Chinese"]
cleanArrests["Asian2"] = sum_column
cleanArrests.head()

del cleanArrests['Asian']

sum_column = cleanArrests['Other inc Chinese'] - cleanArrests['Chinese']
cleanArrests['Other'] = sum_column
cleanArrests.head()

del cleanArrests['Chinese']
del cleanArrests['Other inc Chinese']

del cleanArrests['Any other']

cleanArrests = cleanArrests.rename(columns={'Asian2': 'Asian'})

cleanArrests.head()

del cleanArrests['Bangladeshi']

race = ('White', 'Black', 'Asian', 'Mixed', 'Other', 'Unknown' )
totalArrests = (452320, 60116, 44161, 21832, 9859, 82838)
fig, ax=plt.subplots(figsize = (5,5)) ##creating bar chart
plt.bar(race, totalArrests)
plt.xlabel('Race')
plt.ylabel('Total Arrests')
plt.title('Total Arrests in England and Wales in 2018 by Race')
for i, data in enumerate(totalArrests): ##adding labels to bars
  plt.text(x=i, y=data+1, s=f"{data}", ha='center')

from google.colab import files
uploaded = files.upload()

data_path = "prisonpopuk2.csv"
population = pd.read_csv(data_path, index_col=0)
population.head()

population2 = population.set_index('Unnamed: 1')
population3 = population2.replace(',', '', regex=True) ##REGEX is a way of replacing and cleaning text

population3.head()

population18 = population3['30-Jun-18']

population18.head()

population18.iloc[1:9]

race = ['White', 'Black', 'Asian', 'Mixed', 'Other', 'Unknown']
prisonpop = [60275, 10412, 6635, 3766, 1188, 497]

fig, ax=plt.subplots(figsize = (5,5)) ##creating bar chart
plt.bar(race, prisonpop)
plt.xlabel('Race')
plt.ylabel('Prison Population')
plt.title('Prison Population in England and Wales in 2018 by Race')
for i, data in enumerate(prisonpop): ##adding labels to bars
  plt.text(x=i, y=data+1, s=f"{data}", ha='center') 
plt.show()

from google.colab import files
uploaded = files.upload()

data_path = "entirepopuk.csv"
entirepopulation = pd.read_csv(data_path, index_col=0)
entirepopulation.head()

entirepopulation2 = entirepopulation.drop(labels=['Indian', 'Pakistani', 'Bangladeshi', 'Chinese', 'Asian other', 'Black African', 'Black Caribbean', 'Black other', 'Mixed White/Asian', 'Mixed White/Black African', 'Mixed White/Black Caribbean', 'Mixed other', 'White British', 'White Irish', 'White other', 'White Gypsy/Traveller'])
entirepopulation2.head()

transposedArrests = np.transpose(entirepopulation2)
entirepop = transposedArrests.replace(',', '', regex=True) ##REGEX is a way of replacing and cleaning text
entirepop.head()

del entirepop['Any other']

del entirepop['Arab']

entirepop.head()

r = ['White', 'Black', 'Asian', 'Mixed', 'Other']
greenBars = [452320, 60116, 42872, 21832, 9859]
blueBars = [48209395, 1864890, 4213531, 1224400, 563696]

p1 = plt.bar(r, greenBars)
p2 = plt.bar(r, blueBars, bottom = greenBars)

plt.show()
#plt.show()
## shows arrests against general population

r = ['White', 'Black', 'Asian', 'Mixed', 'Other']
greenBars = [60275, 10412, 6635, 3766, 1188]
blueBars = [48209395, 1864890, 4213531, 1224400, 563696]

p1 = plt.bar(r, greenBars)
p2 = plt.bar(r, blueBars, bottom = greenBars)

plt.show()
#plt.show()
## shows prison pop based on population pop

r = ['White', 'Black', 'Asian', 'Mixed', 'Other']
rawData = {'greenBars':[452320, 60116, 42872, 21832, 9859], 'blueBars':[48209395, 1864890, 4213531, 1224400, 563696]}
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
plt.xlabel("Race/Ethnicity", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.title('Arrests as a % of population in England and Wales', fontsize=14)

plt.ylim(0,30)

plt.show()

##THIS GRAPH shows the number of arrests as a proportion of the population of England / Wales

r = ['White', 'Black', 'Other']
rawData = {'greenBars':[452320, 60116, 42872+21832+9859], 'blueBars':[48209395, 1864890, 4213531+1224400+563696]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = r
plt.bar(r, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

plt.xticks(r, names)
plt.xlabel("Race/Ethnicity", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.title('Arrests as a % of population in England and Wales', fontsize=14)

plt.ylim(0,30)

plt.show()

##THIS GRAPH shows the number of arrests as a proportion of the population of England / Wales

r = ['White', 'Black', 'Other']
rawData = {'greenBars':[452320, 60116, 74563], 'blueBars':[48209395, 1864890, 6001627]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#a3acff', edgecolor='white', width=barWidth)

plt.xticks(r, names)
plt.xlabel("Race")
plt.title('Arrests as a % of population in England and Wales')
plt.show()

##THIS GRAPH shows the number of arrests as a proportion of the population of England / Wales

r = ['White', 'Black', 'Asian', 'Mixed', 'Other']
rawData = {'greenBars':[60275, 10412, 6635, 3766, 1188], 'blueBars':[452320, 60116, 42872, 21832, 9859]}
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
plt.xlabel("Race/Ethnicity", fontsize = 14)
plt.ylabel("Percentage", fontsize = 14)
plt.title("Prison Population as a % of Arrests in England and Wales", fontsize = 14)

plt.ylim(0,30)
plt.show()

r = ['White', 'Black', 'Other']
rawData = {'greenBars':[60275, 10412, 6635+3766+1188], 'blueBars':[452320, 60116, 42872+21832+9859]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = r
plt.bar(r, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

plt.xticks(r, names)
plt.xlabel("Race/Ethnicity", fontsize = 14)
plt.ylabel("Percentage", fontsize = 14)
plt.title("Prison Population as a % of Arrests in England and Wales", fontsize = 14)

plt.ylim(0,30)
plt.show()

df = pd.DataFrame({'r' : ['White', 'Black', 'Asian', 'Mixed', 'Other'],
                   'White' : 452320/48209395*100,
                   'Black' : 60116/1864890*100,
                   'Asian' : 42872/4213531*100,
                   'Mixed' : 21832/1224400*100,
                   'Other' : 9859/563696*100
                   })

categories = list(df)[1:]
N = len(categories)

values=df.loc[0].drop('r').values.flatten().tolist()
values += values[:1]
values

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories, color='grey', size=8)
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

ax.plot(angles, values, linewidth=1, linestyle='solid')
ax.fill(angles, values, 'b', alpha=0.1)

#arrests based on total pop

##Here I was trying to show conversion rate - i.e. prison population as a proportion of arrests BUT it is hard to compare because the only two common groups are white and black...
r2 = ['White', 'Black', 'Asian', 'Mixed', 'Other']
rawData = {'greenBars':[60275, 10412, 6635, 3766, 1188], 'blueBars':[452320, 60116, 42872, 21832, 9859]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r2, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
plt.bar(r2, blueBars, bottom=greenBars, color='#a3acff', edgecolor='white', width=barWidth)
plt.title('Prison population as a proportion of arrests')

plt.xticks(r2)
plt.xlabel("group")
plt.show()

##Here I was trying to show conversion rate - i.e. prison population as a proportion of arrests BUT it is hard to compare because the only two common groups are white and black...
r2 = ['White', 'Black', 'Other']
rawData = {'greenBars':[60275, 10412, 11589], 'blueBars':[452320, 60116, 74563]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r2, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
plt.bar(r2, blueBars, bottom=greenBars, color='#a3acff', edgecolor='white', width=barWidth)
plt.title('Prison population as a proportion of arrests')

plt.xticks(r2)
plt.xlabel("group")
plt.show()