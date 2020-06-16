# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:40:31 2020

@author: zhuxianbin
"""
import pandas as pd
from pandas import Series, DataFrame

data = {'chinese': [68,95,98,90,80], 
        'math':[65,76,86,88,90], 'english':[30,98,88,77,90]}
gdf=DataFrame(data, index = ['zhangfei', 'guanyu', 'liubei', 
                                'dianwei', 'xuchu'])
calculate = gdf.describe().drop(index=['count','25%','50%','75%'])
                    
calculate.loc['var'] = gdf.var()
gdf['all'] = gdf.sum(1)
print(calculate)
print(gdf.sort_values('all', ascending=False))

