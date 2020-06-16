# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:26:07 2020

@author: zhuxianbin
"""
import pandas as pd
import numpy as np

result = pd.read_csv('car_complain.csv')

result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
#print(result.columns)

tags = result.columns[7:]
#print(tags)

#品牌投诉排行
df_brand = result.groupby(['brand'])['id'].agg(['count'])
df_brand =df_brand.sort_values('count', ascending=False)
print('By brand:\n', df_brand)

#车型投诉排行
df_model = result.groupby(['car_model'])['id'].agg(['count'])
df_model = df_model.sort_values('count',ascending = False)
print('By care_model', df_model)

#品牌平均投诉车型排行
df_average = result.groupby(['brand', 'car_model'])['id'].agg(['count']).groupby(['brand']).mean()
df_average = df_average.sort_values('count',ascending = False)
print('By average_car_model:',df_average)




