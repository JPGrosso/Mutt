# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:31:11 2019

@author: juanp
"""

"""Clean the dataset:
Remove the observations where the domestic sales or exports are either negative
 or missing (they appear as “.”) or where the total sales are null or negative.
Filter the dataset in any other way you deem necessary (in each case specify and
 comment the code on your assumptions/reasons for further filtering/cleaning). 
You should end with a balanced panel i.e the dataset should contain firms/companies 
that were seen in each unit of time (see https://en.wikipedia.org/wiki/Panel_data#Example for details). 
Hint: at some point you need to use a `group by`
"""
import pandas as pd

# save filepath to variable for easier access
ine_file_path=(r'C:\Users\juanp\Documents\Mutt\copia de datos_ine.csv')
# read the data and store data in DataFrame titled melbourne_data
ine_data= pd.read_csv(ine_file_path, delimiter=";") 
# print a summary of the data in Melbourne data
ine_data.describe()

print(type(ine_data))

ine_data.head

ine_data.dtypes

#expval=total exports
#fabval=total sales
#domestic sales=fabval-expval?

# Delete the rows within the domestic sales label "." or negative
# For label-based deletion, set the index first on the dataframe:
ine_data = ine_data.set_index("expval")
ine_data = ine_data.drop(".", axis=0) # Delete all rows with label "."



#filtering negative values
cols = ['expval','fabval']
ine_data[cols] = ine_data[ine_data[cols] > 0][cols]
ine_data.dropna()










