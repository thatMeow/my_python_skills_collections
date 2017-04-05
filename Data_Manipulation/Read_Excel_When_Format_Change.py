
# coding: utf-8

# In[1092]:

input_excel_file = 'FB_Volume_2017MA.xlsx'

# make sure you enter the column name the same format as it is in the file. And make sure we have the date values in the file. 
start_column = '2017-01-01' 
end_column = '2019-12-01'


# #### To use this python script, make sure that the key words "Business Line" in the excel file have not changed. Since that is the place where we start reading the data.

# In[1114]:

import pandas as pd
from pandas import DataFrame, Series

import datetime

from xlrd import open_workbook

from IPython.display import HTML

import re

import os


# ### Change to the directory where the .py file is. Put the input excel file in the same folder as the .py file. 

# In[1115]:

curr_path=os.getcwd()
os.chdir(curr_path)


# In[1094]:

def attention(title):
    style = "text-align:left;background:#F7DC6F;padding:30px;color:black;font-size:4em;"
    return HTML('<div style="{}">{}</div>'.format(style, title))


# Find the key words "Business Line" and take it as the starting point. Read the rest of the excel file.

# In[1095]:


book = open_workbook(input_excel_file) # update the excel file name if necessary
for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "Business Line" :
                start_row=rowidx
                start_col=colidx
                sheet_name=sheet.name


# In[1096]:

#Once we get the rowid and colid for the starting cell "Business Line", we can read the file with only the data that we need. 
#Even the cell "Business Line" changes its location, it won't affect our end result
df = pd.read_excel(input_excel_file, sheetname=sheet_name, skiprows=start_row, index_col=start_col)
# df


# In[1097]:

df.head(5)


# #### Drop empty rows and columns from the data set 

# In[1098]:

df.dropna(axis=0, how='all', thresh=None, subset=None, inplace=True)
df.dropna(axis=1, how='all', thresh=None, subset=None, inplace=True)


# #### The original column names for each month contain time. This piece of code format the column names as string.

# In[1099]:

df.index.names = [None]

column_list = [] # an empty list that will take in column names later
for col in df.columns:
    if isinstance(col, datetime.datetime): #
        col=col.date()
        col=str(col) #format column names as string
    else:
        col=str(col) #format column names as string
    column_list.append(col)

df.columns=column_list


# #### Strip heading and trailing white space. I found the "Applications" under "Metric" column have trailing space, that caused trouble when I tried to select rows == "Applications".

# In[1100]:

# # Select string columns only
df_obj = df.select_dtypes(['object'])
# # strip whitespace
df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())


# #### Only need the rows that the 'Metric' column has the following values:
# 
# ######    - Applications, Unit Originations, Average Amount Financed, Total Dollar Originations

# In[1101]:

df = df[df.Metric.isin(['Applications', 'Unit Originations', 'Average Amount Financed', 'Total Dollar Originations'])]


# In[ ]:




# ### Update index names 

# In[1102]:

# get a list of index in the "Metric" column. We will use these lists later. 

unit_origination_list = []
for i, x in enumerate(df.Metric):
    if x == 'Unit Originations':
        unit_origination_list.append(i)

avg_amt_financed_list = []
for i, x in enumerate(df.Metric):
    if x == 'Average Amount Financed':
        avg_amt_financed_list.append(i)
        
total_dollar_orig_list = []
for i, x in enumerate(df.Metric):
    if x == 'Total Dollar Originations':
        total_dollar_orig_list.append(i)


# In[1103]:

# The min(filter(lambda x: x > Dealer_Prime_Index,unit_origination_list)) finds the 1st row for unit origination, avg amt, and total dollar for each section. Even the order or unit orig, avg amt and total dollar changes we can still get the data that we need


index_list = df.index

def find(lst, a):
    
    for i, x in enumerate(lst):
        if x==a:
            return i

# Dealer Prime
Dealer_Prime_Index = find(index_list, '1a. Dealer Prime (excluding NP)')
Dealer_Prime_Units = min(filter(lambda x: x > Dealer_Prime_Index,unit_origination_list)) # find the next index
Dealer_Prime_ATF = min(filter(lambda x: x > Dealer_Prime_Index,avg_amt_financed_list))
Dealer_Prime_Dollars = min(filter(lambda x: x > Dealer_Prime_Index,total_dollar_orig_list))

df.index.values[Dealer_Prime_Units] = 'Dealer_Prime_Units'
df.index.values[Dealer_Prime_ATF] = 'Dealer_Prime_ATF'
df.index.values[Dealer_Prime_Dollars] = 'Dealer_Prime_Dollars'


#Dealer Near Prime
Dealer_Near_Prime_Index = find(index_list, '1b. Dealer Near Prime')
Dealer_Near_Prime_Units = min(filter(lambda x: x > Dealer_Near_Prime_Index,unit_origination_list)) # find the next index
Dealer_Near_Prime_ATF = min(filter(lambda x: x > Dealer_Near_Prime_Index,avg_amt_financed_list))
Dealer_Near_Prime_Dollars = min(filter(lambda x: x > Dealer_Near_Prime_Index,total_dollar_orig_list))

df.index.values[Dealer_Near_Prime_Units] = 'Dealer_Near_Prime_Units'
df.index.values[Dealer_Near_Prime_ATF] = 'Dealer_Near_Prime_ATF'
df.index.values[Dealer_Near_Prime_Dollars] = 'Dealer_Near_Prime_Dollars'


#Core
Core_Index = find(index_list, '2. Core')
Core_Units = min(filter(lambda x: x > Core_Index,unit_origination_list)) # find the next index
Core_ATF = min(filter(lambda x: x > Core_Index,avg_amt_financed_list))
Core_Dollars = min(filter(lambda x: x > Core_Index,total_dollar_orig_list))

df.index.values[Core_Units] = 'Core_Units'
df.index.values[Core_ATF] = 'Core_ATF'
df.index.values[Core_Dollars] = 'Core_Dollars'


#Core
Core_Index = find(index_list, '2. Core')
Core_Units = min(filter(lambda x: x > Core_Index,unit_origination_list)) # find the next index
Core_ATF = min(filter(lambda x: x > Core_Index,avg_amt_financed_list))
Core_Dollars = min(filter(lambda x: x > Core_Index,total_dollar_orig_list))

df.index.values[Core_Units] = 'Core_Units'
df.index.values[Core_ATF] = 'Core_ATF'
df.index.values[Core_Dollars] = 'Core_Dollars'


#Carmax
Carmax_Index = find(index_list, '3. Carmax')
Carmax_Units = min(filter(lambda x: x > Carmax_Index,unit_origination_list)) # find the next index
Carmax_ATF = min(filter(lambda x: x > Carmax_Index,avg_amt_financed_list))
Carmax_Dollars = min(filter(lambda x: x > Carmax_Index,total_dollar_orig_list))

df.index.values[Carmax_Units] = 'Carmax_Units'
df.index.values[Carmax_ATF] = 'Carmax_ATF'
df.index.values[Carmax_Dollars] = 'Carmax_Dollars'


#PA
PA_Index = find(index_list, '4. PA')
PA_Units = min(filter(lambda x: x > PA_Index,unit_origination_list)) # find the next index
PA_ATF = min(filter(lambda x: x > PA_Index,avg_amt_financed_list))
PA_Dollars = min(filter(lambda x: x > PA_Index,total_dollar_orig_list))

df.index.values[PA_Units] = 'PA_Units'
df.index.values[PA_ATF] = 'PA_ATF'
df.index.values[PA_Dollars] = 'PA_Dollars'


#Refi
Refi_Index = find(index_list, 'Total DIRECT (5+6) EXCLUDING AN')
Refi_Units = min(filter(lambda x: x > Refi_Index,unit_origination_list)) # find the next index
Refi_ATF = min(filter(lambda x: x > Refi_Index,avg_amt_financed_list))
Refi_Dollars = min(filter(lambda x: x > Refi_Index,total_dollar_orig_list))

df.index.values[Refi_Units] = 'Refi_Units'
df.index.values[Refi_ATF] = 'Refi_ATF'
df.index.values[Refi_Dollars] = 'Refi_Dollars'


#Prime_AN
Prime_AN_Index = find(index_list, '10. Prime Auto Navigator')
Prime_AN_Units = min(filter(lambda x: x > Prime_AN_Index,unit_origination_list)) # find the next index
Prime_AN_ATF = min(filter(lambda x: x > Prime_AN_Index,avg_amt_financed_list))
Prime_AN_Dollars = min(filter(lambda x: x > Prime_AN_Index,total_dollar_orig_list))

df.index.values[Prime_AN_Units] = 'Prime_AN_Units'
df.index.values[Prime_AN_ATF] = 'Prime_AN_ATF'
df.index.values[Prime_AN_Dollars] = 'Prime_AN_Dollars'


#Near_Prime_AN
Near_Prime_AN_Index = find(index_list, '11. Near Prime Auto Navigator')
Near_Prime_AN_Units = min(filter(lambda x: x > Near_Prime_AN_Index,unit_origination_list)) # find the next index
Near_Prime_AN_ATF = min(filter(lambda x: x > Near_Prime_AN_Index,avg_amt_financed_list))
Near_Prime_AN_Dollars = min(filter(lambda x: x > Near_Prime_AN_Index,total_dollar_orig_list))

df.index.values[Near_Prime_AN_Units] = 'Near_Prime_AN_Units'
df.index.values[Near_Prime_AN_ATF] = 'Near_Prime_AN_ATF'
df.index.values[Near_Prime_AN_Dollars] = 'Near_Prime_AN_Dollars'


#Near_Prime_AN
Near_Prime_AN_Index = find(index_list, '12. Core Auto Navigator')
Near_Prime_AN_Units = min(filter(lambda x: x > Near_Prime_AN_Index,unit_origination_list)) # find the next index
Near_Prime_AN_ATF = min(filter(lambda x: x > Near_Prime_AN_Index,avg_amt_financed_list))
Near_Prime_AN_Dollars = min(filter(lambda x: x > Near_Prime_AN_Index,total_dollar_orig_list))

df.index.values[Near_Prime_AN_Units] = 'Near_Prime_AN_Units'
df.index.values[Near_Prime_AN_ATF] = 'Near_Prime_AN_ATF'
df.index.values[Near_Prime_AN_Dollars] = 'Near_Prime_AN_Dollars'


#Core_AN
Core_AN_Index = find(index_list, '12. Core Auto Navigator')
Core_AN_Units = min(filter(lambda x: x > Core_AN_Index,unit_origination_list)) # find the next index
Core_AN_ATF = min(filter(lambda x: x > Core_AN_Index,avg_amt_financed_list))
Core_AN_Dollars = min(filter(lambda x: x > Core_AN_Index,total_dollar_orig_list))

df.index.values[Core_AN_Units] = 'Core_AN_Units'
df.index.values[Core_AN_ATF] = 'Core_AN_ATF'
df.index.values[Core_AN_Dollars] = 'Core_AN_Dollars'


#Auto_Finance
Auto_Finance_Index = find(index_list, 'Overall COAF')
Auto_Finance_Units = min(filter(lambda x: x > Auto_Finance_Index,unit_origination_list)) # find the next index
Auto_Finance_ATF = min(filter(lambda x: x > Auto_Finance_Index,avg_amt_financed_list))
Auto_Finance_Dollars = min(filter(lambda x: x > Auto_Finance_Index,total_dollar_orig_list))

df.index.values[Auto_Finance_Units] = 'Auto_Finance_Units'
df.index.values[Auto_Finance_ATF] = 'Auto_Finance_ATF'
df.index.values[Auto_Finance_Dollars] = 'Auto_Finance_Dollars'


# In[1104]:

df = df[df.Metric.isin(['Unit Originations', 'Average Amount Financed', 'Total Dollar Originations'])]


# In[1105]:

end_index_list = ['Auto_Finance_Units',
                  'Auto_Finance_ATF',
                  'Auto_Finance_Dollars',
                  'Carmax_Units',
                  'Carmax_ATF',
                  'Carmax_Dollars',
                  'Core_Units',
                  'Core_ATF',
                  'Core_Dollars',
                  'Core_AN_Units',
                  'Core_AN_ATF',
                  'Core_AN_Dollars',
                  'Dealer_Near_Prime_Units',
                  'Dealer_Near_Prime_ATF',
                  'Dealer_Near_Prime_Dollars',
                  'Dealer_Prime_Units',
                  'Dealer_Prime_ATF',
                  'Dealer_Prime_Dollars',
                  'Near_Prime_AN_Units',
                  'Near_Prime_AN_ATF',
                  'Near_Prime_AN_Dollars',
                  'PA_Units',
                  'PA_ATF',
                  'PA_Dollars',
                  'Prime_AN_Units',
                  'Prime_AN_ATF',
                  'Prime_AN_Dollars',
                  'Refi_Units',
                  'Refi_ATF',
                  'Refi_Dollars'                
                 ]


# In[1106]:

# only take the rows that we need
df = df.loc[end_index_list]
# specify the range of dates that you need
df = df.ix[:,start_column:end_column]
# convert all data to float type
# df = df.astype(float)
df = df.T
df.head()


# In[1107]:

df.head(5)


# In[ ]:




# ### Reshape the dataframe to match Steven Moen's table structure. Using "rsplit" to split the words, "stack" to reshape the dataframe

# In[1108]:

df.columns = df.columns.str.rsplit("_", n=1, expand=True)
df = df.stack(level=0).rename_axis((None, "Segment")).reset_index("Segment")

df['Segment'] = df['Segment'].str.replace('_',' ')



# In[1109]:

# df['segment4_2'] = ['Auto_Finance' if x == 'Auto Finance' else '' for x in df['Segment']]

def f(row):
    if row['Segment'] == "Auto Finance":
        val = "Auto_Finance"
    elif row['Segment'] == "Carmax":
        val = "Dealer_Subprime"
    elif row['Segment'] == "Core":
        val = "Dealer_Subprime"  
    elif row['Segment'] == "Core AN":
        val = "Dealer_Subprime"
    elif row['Segment'] == "Dealer Near Prime":
        val = "Near_Prime"
    elif row['Segment'] == "Dealer Prime":
        val = "Dealer_Prime"
    elif row['Segment'] == "Near Prime AN":
        val = "Near_Prime"
    elif row['Segment'] == "PA":
        val = "Dealer_Subprime"
    elif row['Segment'] == "Prime AN":
        val = "Dealer_Prime"
    elif row['Segment'] == "Refi":
        val = "Direct"
    else:
        val = ''
    return val

df['segment4_2'] = df.apply(f, axis=1)


# In[1110]:

df.head(5)


# ### Format Columns 

# In[1111]:

df['ATF'] = (df['ATF']).apply(lambda x: '${:,.2f}'.format(x))
df['Dollars'] = (df['Dollars']).apply(lambda x: '${:,.2f}'.format(x))
df['Units'] = (df['Units']).apply(lambda x: '{:,.2f}'.format(x))

df.index = pd.to_datetime(df.index).strftime('%d%b%Y')


# In[1112]:

df.to_excel('result_mimicing_sas.xlsx')


# In[1113]:

df


# In[ ]:




# In[ ]:




# In[ ]:



