# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:34:59 2021

@author: Lenovo
"""

import pandas as pd

dencodt=  pd.read_csv('20denco.csv')
dencodt


#ans 1
dencodt['custname'].value_counts().head(10)


# ans 2 

dt=dencodt.groupby('custname',as_index=True).agg({'revenue':'sum'})

#dencodt.pivot_table('revenue', index='custname', aggfunc='sum')

dt.sort_values('revenue',ascending=False)


# ans 3 

dencodt.columns
dencodt.groupby('partnum').agg({'revenue':'sum'}).sort_values('revenue',ascending=False)


# ans 4 

dencodt.groupby('partnum').agg({'margin':'sum'}).sort_values('margin',ascending=False)


# ans 5 

dencodt.groupby('custname').agg({'revenue':'sum'}).sort_values('revenue',ascending=False)


# ans 6 and ans 7 , same as above answers
