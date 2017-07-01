# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 11:02:13 2016

@author: X
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # linear algebra
import seaborn as sbn

zika = pd.read_csv('cdc_zika.csv',parse_dates=['report_date'],infer_datetime_format=True,index_col=0)


zika_lab_pos = zika[zika['data_field'] =='zika_lab_positive']


locations =list(set(zika_lab_pos['location']))


loc_counts = {}

for loc in zika_lab_pos['location']:
    if loc in loc_counts:
        loc_counts[loc]+= 1
    else:
        loc_counts[loc]=1


counts_zika_locations = zika.location.value_counts()

counts_zika_locations[:30].plot(kind='bar', figsize=(12, 7))

plt.title("Number of locations reported - Top 30")

symptoms = ['confirmed_fever',
       'confirmed_acute_fever', 'confirmed_arthralgia',
       'confirmed_arthritis', 'confirmed_rash', 'confirmed_conjunctivitis',
       'confirmed_eyepain', 'confirmed_headache', 'confirmed_malaise']
       
fig = plt.figure(figsize=(13,13))
for symptom in symptoms:
    zika[zika.data_field == symptom].value.plot()
plt.legend(symptoms, loc='best')
plt.title('Understanding symptoms of zika virus')

plt.show()


age_groups = ('confirmed_age_under_1', 'confirmed_age_1-4',
       'confirmed_age_5-9', 'confirmed_age_10-14', 'confirmed_age_15-19',
       'confirmed_age_20-24', 'confirmed_age_25-34', 'confirmed_age_35-49',
       'confirmed_age_50-59', 'confirmed_age_60-64',
       'confirmed_age_60_plus')
       
       
zika[zika.data_field == "confirmed_male"].value.plot()

zika[zika.data_field == "confirmed_female"].value.plot().legend(("Male","Female"),loc="best")

plt.title("Confirmed Male vs Female cases")


plt.show()
sbn.set_style("whitegrid")

print(zika.groupby("location").size().reset_index().rename(columns={0: "count"}))
zika.groupby("location").size().reset_index().rename(columns={0: "count"})

##looking at zika cases by country
locations = set(zika['location'])
loc_val = zika[['location','value']]
loc_1 = 'United_States_Virgin_Islands'
loc_val[loc_val.location == loc_1].value.plot(style=['o','rx'])
plt.title(loc_1)

grouped_locations = zika.groupby("location").size().reset_index().rename(columns={0: "count"})
grouped_locations.sort(columns = 'count',ascending = False)[:30].plot(kind = 'bar',x = 'location',figsize=(12, 7))

plt.show()

#look at the most common symptom per location, o


grouped_data_field = zika.groupby("data_field").size().reset_index().rename(columns={0: "count"})
grouped_data_field.sort(columns = 'count',ascending = False)[:30].plot(kind = 'bar',x = 'data_field')

top_5_location = ['United_States_Virgin_Islands','El_Salvador','Puerto_Rico','Ecuador','Dominican_Republic']
grouped_locations = zika.groupby("location").size().reset_index().rename(columns={0: "count"})
grouped_locations.sort(columns = 'count',ascending = False)[:30].plot(kind = 'bar',x = 'location')

for loc in top_5_location:
    zika_loc_temp = zika[zika['location']==loc].groupby("data_field").size().reset_index().rename(columns={0: "count"})
    zika_loc_temp.sort(columns = 'count',ascending = False)[:30].plot(kind = 'bar',x = 'data_field',title = loc,figsize=(12, 7))
