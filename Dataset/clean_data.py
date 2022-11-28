import pandas as pd
import numpy as np


###  Single-Race Population Estimates 2010-2019 ###
''
#from txt to csv
Df = pd.read_csv('Single-Race Population Estimates 2010-2019.txt', sep="\t")

#Delete useless columns and rename
Df = Df[['State', 'Gender', 'Ethnicity', 'Race', 'Yearly July 1st Estimates', 'Population']]
Df = Df.rename(columns={'Yearly July 1st Estimates': 'Year'})
Df= Df.sort_values(by='Year')
Df = Df.reset_index(drop=True)

Df.to_csv('Single-Race Population Estimates 2010-2019.csv')''

###  Multiple Cause of Death, 1999-2020 ###

#from txt to csv

Df = pd.read_csv('Multiple Cause of Death, 1999-2020.txt', sep="\t")

#Delete useless columns and rename
Df = Df[['State', 'Gender', 'Year', 'Deaths']]
Df= Df.sort_values(by='Year')
Df = Df.reset_index(drop=True)
# if there are zero deaths the value is "suppressed", so we search all these cells and
# change their value to 0
for i in range(Df['Deaths'].size):
    if Df.at[i,'Deaths'] == 'Suppressed':
        Df.at[i,'Deaths'] = 0

Df.to_csv('Multiple Cause of Death, 1999-2020.csv')
print(Df)

