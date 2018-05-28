#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:01:52 2018

@author: alexanderpavlushkin
"""

import pandas as pd
df = pd.read_csv('mv_hosp_chance.txt')
df = pd.read_csv('mv_hosp_chance.txt', index_col='org')

# df.head() 
# cols = df.columns

# change an index
xf = df.set_index('author')
df.info()
xf.info()
xf.head()

df.iloc[0:1,7:10]

df[['apgar','author']] # selecting only some colums

df.loc[:,'apgar':'author'] # selecting only some colums with slicing

df.shape
df.dropna(how='all').shape
df.dropna(how='any').shape

# transform days to months
hc_age_months =  df[['hc_age']].apply(lambda n: n//12)
hc_age_months.columns = ['mnths']
print(hc_age_months.head())

# adding column to given dataframe
df['mnths'] = hc_age_months
print(df.head())

df.index

# using of map function
df.apgar.map({0:'bad'})

# setting simple numeric index
df.index = range(len(df))

# Ierarchial indexing
sales = sales.set_index(['state', 'month'])
# Sort the MultiIndex: sales
sales = sales.sort_index()

# multiindex to df
df = df.set_index(['org','hosp_in'])
df = df.sort_index()

# dealing with json
import json

x = df.author[0]
type(x)

y = json.loads(x)
type(y)

y.keys()
y['full_name']

# multiindexing script
df['org_dict'] = json.loads(df.org)

# get org from json
def get_simple_str(source_col,key_name) :
    arr = []
    for i in source_col:
        
        d = json.loads(i)
        arr.append(d[key_name])
    return(arr)
        
df['org_dict'] = get_simple_str(df['org'],'caption')

df['org_dict'].unique()

# replace names to labels
orgs = ['ГБУЗ "Самарский Областной Клинический кардиологический Диспансер"',
       'ФГБУ "ФЦССХ" Минздрава РФ (г. Красноярск)',
       'Детская городская больница №1 (г. С.-Петербург)',
       'ФГБУ "ФЦССХ" Минздрава РФ (г. Астрахань)',
       'ФГБУ "ФЦССХ" Минздрава РФ (г. Челябинск)',
       'ГАУ "Национальный Научно-Практический Центр Здоровья Детей" МЗ РФ',
       'Научно-исследовательский институт кардиологии (г. Томск)',
       'Национальный научно-практический центр сердечно-сосудистой хирургии им. А.Н. Бакулева',
       'Окружной кардиологический диспансер Центр диагностики и сердечно-сосудистой хирургии (г. Сургут 2)',
       'ФГБУ "ФЦССХ" Минздрава РФ (г. Хабаровск)',
       'ФГБУ "ФЦССХ" Минздрава РФ (г. Пермь)']

labels = ['SAMD',
       'KRSK',
       'SPBD',
       'ASTR',
       'CHEL',
       'NCZD',
       'TMSK',
       'BKLV',
       'SRGT',
       'KHAB',
       'PERM']

org_ref = dict(zip(orgs,labels))

df['org_dict']

df['org_dict'] = df['org_dict'].map(org_ref)

# authors
df['man'] = get_simple_str(df['author'],'full_name')

# multiindex
dfi = df.set_index(['org_dict','man'])
dfi = dfi.sort_index()
dfi.loc['KRSK','Ильин Алексей Сергеевич']
dfi.loc[slice('CHEL','SPBD'),slice(None)]

# pivot 
visitors_pivot = users.pivot(index='weekday',
                            columns='city',
                            values='visitors')


# pivot table
 more_trials.pivot_table(index='treatment',
 ...: columns='gender',
 ...: values='response',
 ...: aggfunc='count')


tab_for_pivot = df.loc[:,['org_dict','man','apgar','ivl_duration']]

pvt1 = tab_for_pivot.pivot_table(index='org_dict', columns='apgar', aggfunc='count')


# groupby
def spread(series):
    return series.max() - series.min()

dfgb = dfi.groupby(['org_dict','man'])['apgar','hc_age','ivl_duration']
dfgb.mean()
aggregator = {'apgar':'max','ivl_duration':spread,'hc_age':('count','min',spread)}
dfgb.agg(aggregator)





# simplifying dates
df['date'] df['date_ins'].dt.date

date= pd.to_datetime('2017-06-08 09:20:20.326839+00').date()