#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:52:57 2024

@author: dianachapter
"""

import pandas as pd

#file = pd.read_csv("data_01/insurance_data.csv", delimiter='\t', header=None)
#file = pd.read_csv("data_01/insurance_data.csv",skiprows = 5)
#file = pd.read_csv("data_01/iris.csv")

column_names = ["A","B","C"]
file = pd.read_csv("data_01/housing_data.csv", names = column_names)
df = pd.DataFrame(file)

print(df.info())
print(df.describe())
