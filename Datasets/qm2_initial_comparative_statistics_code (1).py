# Code for generating Initial Comparative Statistics visualisations

from google.colab import files

files.upload()

# Commented out IPython magic to ensure Python compatibility.
import pandas
import pylab
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('ggplot')

pylab.rcParams['figure.figsize'] = (10., 8.)

import numpy as np

ics_data = pandas.read_csv('Initial Comparative Data.csv', index_col=0)

ics_data.head()

# 26-64 "Populations by Ethnicity"

N = 5

whitepop = (ics_data['White Pop %'].loc['England and Wales'],
            ics_data['White Pop %'].loc['Florida'],
            ics_data['White Pop %'].loc['Massachusetts'],
            ics_data['White Pop %'].loc['Oregon'],
            ics_data['White Pop %'].loc['South Dakota'])
blackpop = (ics_data['Black Pop %'].loc['England and Wales'],
            ics_data['Black Pop %'].loc['Florida'],
            ics_data['Black Pop %'].loc['Massachusetts'],
            ics_data['Black Pop %'].loc['Oregon'],
            ics_data['Black Pop %'].loc['South Dakota'])
whiteandblackpop = (100-ics_data['Other Pop %'].loc['England and Wales'],
                    100-ics_data['Other Pop %'].loc['Florida'],
                    100-ics_data['Other Pop %'].loc['Massachusetts'],
                    100-ics_data['Other Pop %'].loc['Oregon'],
                    100-ics_data['Other Pop %'].loc['South Dakota'])
otherpop = (ics_data['Other Pop %'].loc['England and Wales'],
            ics_data['Other Pop %'].loc['Florida'],
            ics_data['Other Pop %'].loc['Massachusetts'],
            ics_data['Other Pop %'].loc['Oregon'],
            ics_data['Other Pop %'].loc['South Dakota'])

ind = np.arange(N)
width = 0.8  

ax = plt.subplot(111)

p1 = plt.bar(ind, whitepop, width, color='#7F8DA8')
p2 = plt.bar(ind, blackpop, width,
             bottom=whitepop, color='#FADFC3')
p3 = plt.bar(ind, otherpop, width, bottom=whiteandblackpop, color='#E84D60')

plt.ylabel('% of Population')
plt.title('Populations by Ethnicity')
plt.xticks(ind, ('E+W', 'Florida', 'Massachusetts', 'Oregon', 'S. Dakota'))
plt.yticks(np.arange(0, 101, 10))

plt.legend((p1[0], p2[0], p3[0]), ('White Population', 'Black Population', 'Other Population'), bbox_to_anchor=(0.5, -0.2), loc='lower center')

plt.show()

# 68-86 = "Populations by Number"

N = 5

totalpop = (ics_data['Total Pop Mill'].loc['England and Wales'],
            ics_data['Total Pop Mill'].loc['Florida'],
            ics_data['Total Pop Mill'].loc['Massachusetts'],
            ics_data['Total Pop Mill'].loc['Oregon'],
            ics_data['Total Pop Mill'].loc['South Dakota'])

ind = np.arange(N)
width = 0.8  
#
p1 = plt.bar(ind, totalpop, width, color='#E84D60')

plt.ylabel('Population Size (in millions)')
plt.title('Populations by Number')
plt.xticks(ind, ('E+W', 'Florida', 'Massachusetts', 'Oregon', 'S. Dakota'))
plt.yticks(np.arange(0, 61, 5))

plt.show()

# 90-116 "Arrest and Incarceration Rates"

N = 5

arrestrates = (ics_data['Arrest Rate'].loc['England and Wales'],
            ics_data['Arrest Rate'].loc['Florida'],
            ics_data['Arrest Rate'].loc['Massachusetts'],
            ics_data['Arrest Rate'].loc['Oregon'],
            ics_data['Arrest Rate'].loc['South Dakota'])

incarcerationrates = (ics_data['Incarcerated Rate'].loc['England and Wales'],
            ics_data['Incarcerated Rate'].loc['Florida'],
            ics_data['Incarcerated Rate'].loc['Massachusetts'],
            ics_data['Incarcerated Rate'].loc['Oregon'],
            ics_data['Incarcerated Rate'].loc['South Dakota'])

ind = np.arange(N)
width = 0.35  

p1 = plt.bar(ind, arrestrates, width, color='#E84D60', label = 'Arrests')
p2 = plt.bar(ind+width, incarcerationrates, width, color='#7F8DA8', label = 'Arrests')

plt.ylabel('Rate per 100,000')
plt.title('Arrest and Incarceration Rates')
plt.xticks(ind + width / 2)
plt.xticks(ind, ('E+W', 'Florida', 'Massachusetts', 'Oregon', 'S. Dakota'))
plt.yticks(np.arange(0, 4001, 250))

plt.show()
