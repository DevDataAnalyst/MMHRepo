#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import xlsxwriter

data = pd.read_excel('Budget.xlsx',sheet_name='DC New Template (BU Wise) (3)')
data.fillna(0,inplace=True)

new_colums = data.columns
new_colums = new_colums.insert(1,'Month')

master_data = pd.DataFrame(columns=new_colums)

month_list = ['APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','JAN','FEB','MAR']

def rowTranformation(row):
    global master_data
    temp = pd.DataFrame(columns=new_colums)
    for i in range(12):
        val = []
        val.append(row[new_colums[0]])
        val.append(month_list[i])
        for j in new_colums[2:]:
            val.append(round(row[j]/12,2))
        temp.loc[i] = val
    master_data = master_data.append(temp,ignore_index=True)

    
data.apply(lambda x: rowTranformation(x),axis=1)
master_data.to_excel('output.xlsx',sheet_name='MonthlyView',index=False)

