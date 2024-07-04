import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\HP\Desktop\New folder\Project_1\my_venv\Financial Analytics data.csv')

print(df)

df.index = df['S.No.']
print(df)

columns = list(df)
print(columns)

print(df.isnull().sum())

# Changing the name of columns temporarily for ease of code

df.columns = ['S.No.', 'Name', 'Mar Cap - Crore', 'S1', 'S2']
print(df)

# Defining a function to check if a value is numerical
def is_numerical(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Shifting numerical values from S2 to empty spaces in S1
for index, row in df.iterrows():
    if pd.isnull(row['S1']) or row['S1'] == '':
        if not pd.isnull(row['S2']) and is_numerical(row['S2']):
            df.at[index, 'S1'] = row['S2']
            df.at[index, 'S2'] = np.nan  # Setting the moved value in S2 to NaN




# Dropping empty column S2
df.drop(['S2'], axis=1, inplace = True)
print(df)

# Saving the modified DataFrame back to a CSV file 
df.to_csv('df_modified.csv', index=False)
print(df)

print(df.isnull().sum())

# Replacing NAN values in S1 and Market Cap - Crores with their median(right skewed)
col = df['Mar Cap - Crore']
col = col.fillna(col.median(), inplace = True)

col = df['S1']
col = col.fillna(col.median(), inplace = True)
print(df.isnull().sum())

# Changing the name of columns temporarily for ease of code
df.columns = ['S.No.', 'Name', 'Mar Cap - Crore', 'Sales Qtr - Crore']
print(df)

# Checking if there are any zero values in Sales Qtr - Crore column 
for index, row in df.iterrows():
    if row['Sales Qtr - Crore'] == 0:
        print('There are zero value')
df['Sales Qtr - Crore'].replace(0, np.nan, inplace=True) # Replacing zero values with nan values

# Saving the modified DataFrame back to a CSV file 
df.to_csv('df_modified.csv', index=False)
print(df)

# Sorting Market Capitalization in descending orded
df_sort_descend = df.sort_values(by='Mar Cap - Crore', ascending = False)
print(df_sort_descend.head())

# Dividing them into Small Cap, Mid Cap and large Cap companies
df.insert(4, 'Cap Size', None) 
print(df)

for index, row in df.iterrows():
    if row['Mar Cap - Crore'] >= 20000:
        df.loc[index, 'Cap Size'] = 'Large'
    elif row['Mar Cap - Crore'] >= 5000:
        df.loc[index, 'Cap Size'] = 'Mid'
    else:
        df.loc[index, 'Cap Size'] = 'Small'

print(df)

# Calculating Average Sales
avg_sales = df['Sales Qtr - Crore'].sum()/len(df['Sales Qtr - Crore'])
print(' Average Sales : {} Cr'.format(round(avg_sales), 2))

# Count of total Small, Mid and Large Cap companies
cap_count = df['Cap Size'].value_counts()
print(cap_count)

# Creating a new column of Price-to-Sales(P/S) ratio
df.insert(4, 'Price-to-Sales ratio(P/S)', None)

for index, row in df.iterrows():
    df.loc[index, 'Price-to-Sales ratio(P/S)'] = row['Mar Cap - Crore'] / row['Sales Qtr - Crore']

print(df)

df.to_csv('df_modified.csv', index=False )








