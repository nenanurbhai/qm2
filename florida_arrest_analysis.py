# -*- coding: utf-8 -*-
"""FLORIDA Arrest Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FSzX-QmFmetBl6lHL7PwZMMFZKSc6haL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from math import pi

###THIS DATA DOES NOT SEPARATE WHITE/BLACK INTO HISPANIC - WORKS FROM APPEARANCE ALONE.
###SO WE DO NOT SEPARATE THE POPULATION DATA INTO HISPANIC EITHER.

from google.colab import files
uploaded = files.upload()

data_path = "Florida2019.csv"
arrests = pd.read_csv(data_path, index_col=0)
#arrests.loc[' STATEWIDE TOTAL']
arrests.head()

#arrests.isnull().sum()
newArrests = arrests.fillna(" ")
newArrests.isnull().sum() ##Checking for and removing any null values

transposedArrests = np.transpose(newArrests)
cleanArrests = transposedArrests.replace(',', '', regex=True) ##REGEX is a way of replacing and cleaning text
cleanArrests[' STATEWIDE TOTAL'].loc['Total Arrests WHITE':'Total Arrests ASIAN']

race = ['White', 'Black', 'Indian', 'Asian']
totalArrests = [437950, 235770, 1177, 4324]

fig, ax=plt.subplots(figsize = (5,5)) ##creating bar chart
plt.bar(race, totalArrests)
plt.xlabel('Race')
plt.ylabel('Total Arrests')
plt.title('Total Arrests in Florida in 2019 by Race')
for i, data in enumerate(totalArrests): ##adding labels to bars
  plt.text(x=i, y=data+1, s=f"{data}", ha='center') 
plt.show()

data_path = "FloridaPopulation.csv"
population = pd.read_csv(data_path, index_col=0)
population.head()
population['PopNumber'].loc['White alone, percent':'Two or More Races, percent']

r = ['White', 'Black', 'Indian', 'Asian']
greenBars = [437950, 235770, 1177, 4324]
blueBars = [16602290.7, 3629737.55, 107388.685, 644332.11]

p1 = plt.bar(r, greenBars)
p2 = plt.bar(r, blueBars, bottom = greenBars)

#plt.show()
##THIS GRAPH IS NOT NORMALISED AND IS NOT GOOD FOR MAKING COMPARISON

r = ['White', 'Black', 'Indian', 'Asian']
rawData = {'greenBars':[437950, 235770, 1177, 4324], 'blueBars':[16602290.7, 3629737.55, 107388.685, 644332.11]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = race
plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#a3acff', edgecolor='white', width=barWidth)

plt.title("Arrests as % of Population in Florida")
plt.xticks(r, names)
plt.xlabel("Race")
plt.show()

##THIS GRAPH shows the number of arrests as a proportion of the population of Florida

r = ['White', 'Black', 'Other']
rawData = {'greenBars':[437950, 235770, 1177+4324], 'blueBars':[16602290.7, 3629737.55, 107388.685+644332.11]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = r
plt.bar(r, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

plt.ylim(0,30)
plt.title("Arrests as % of Population in Florida", fontsize=14)
plt.xticks(r, names)
plt.xlabel("Race", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.show()

data_path = "FloridaPopu.csv"
population = pd.read_csv(data_path, index_col=0)
population.loc['Population']

##Here I was trying to show conversion rate - i.e. prison population as a proportion of arrests BUT it is hard to compare because the only two common groups are white and black...
##The OTHER category represents Hispanics and any other race apart from White/Black BUT the arrests data does not divide white/black into Hispanic so the two are not comparable!!!!:/
r = ['White', 'Black', 'Other']
rawData = {'greenBars':[38419, 44826, 11958+423], 'blueBars':[437950, 235770, 1177+4324]}
df = pd.DataFrame(rawData)

totals = [i+j for i,j in zip(df['greenBars'], df['blueBars'])]
greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

fig, ax=plt.subplots(figsize = (5,10))
barWidth = 0.85
names = r
plt.bar(r, greenBars, color='#7F8DA8', edgecolor='white', width=barWidth)
plt.bar(r, blueBars, bottom=greenBars, color='#FADFC3', edgecolor='white', width=barWidth)

#plt.ylim(0,30)
plt.title("Prison Population as % of Arrests in Florida", fontsize=14)
plt.xticks(r, names)
plt.xlabel("Race", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.show()
