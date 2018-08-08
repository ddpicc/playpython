#!/usr/bin/env python
#coding: utf-8

import pandas as pd

data = pd.read_csv('records.csv',sep='\t')
count = len(data)
print(count)
print(data.head(5))
print(data['火山号'].head(5))
