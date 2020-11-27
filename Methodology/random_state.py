import random 
north_east = ["Connecticut", "Delaware", "Maine", "Massachusetts", "Maryland", "New Hampshire", \
              "New Jersey", "New York", "Pennsylvania", "Rhode Island", "Vermont"]

midwest = ["North Dakota", "South Dakota", "Illinois", "Indiana", "Iowa","Kansas", "Michigan", \
           "Minnesota", "Missouri","Nebraska", "Ohio", "Wisconsin"]

west = ["Arizona", "California", "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", \
         "Oregon", "Utah", "Washington", "Wyoming"]

south = ["Alabama", "Arkansas", "Delaware", "Florida", "Georgia", "Kentucky", "Louisiana", \
         "Maryland", "Mississippi", "North Carolina", "Oklahoma", "South Carolina", \
         "Tennessee", "Texas", "Virginia", "West Virginia"]

print("The state from North East we'll use is", random.choice(north_east))
print("The state from Midwest we'll use is", random.choice(midwest))
print("The state from West we'll use is", random.choice(west))
print("The state from South we'll use is", random.choice(south))

ALTERNATIVE:

import random

random.seed(1)
print("The state representing the North-East is:", random.choice(['Maine', 'New Hampshire', 'Massachusetts', 'Vermont','New York',
                                                                  'New Jersey', 'Pennsylvania', 'Connecticut', 'Rhode Island']))

random.seed(1)
print("The state representing the Midwest is:", random.choice(['Illinois', 'Indiana', 'South Dakota', 'Ohio', 'Wisconsin', 'Iowa',
                                                               'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Michigan']))

random.seed(1)
print("The state representing the West is:", random.choice(['Arizona', 'Colorado', 'Oregon', 'Montana', 'Nevada', 'New Mexico',
                                                            'Utah', 'Wyoming', 'Alaska', 'California', 'Hawaii', 'Idaho', 'Washington']))

random.seed(1)
print("The state representing the South is:", random.choice(['Delaware', 'North Carolina', 'Georgia', 'Maryland', 'Florida', 'South Carolina',
                                                             'Virginia', 'Washington D.C.', 'West Virginia', 'Alabama', 'Kentucky', 'Mississippi', 
                                                             'Tennessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas']))
