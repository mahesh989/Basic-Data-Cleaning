import numpy as np
import pandas as pd


#Reading data from the URL
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
df = pd.read_csv(url, sep='\t')



'''this will give the first and last four entries of the dataset'''
df['choice_description'].head(100)
df.tail(10)


# this will give the column names and respective datatype an organized manner
for column, dtype in zip(df.columns, df.dtypes):
    print(f"{column}:{dtype}")
    

# For example,item_price contain dollor sign, so we can remove it and replace the datatype into int64. 

df['item_price'] = df['item_price'].str.replace('$', '')
#Let's check the price
print(df['item_price'].head(10))

#change datatype
df['item_price'] = df['item_price'].astype('float64')

#Let's check the datatype again
for column, dtype in zip(df.columns, df.dtypes):
    print(f"{column}:{dtype}")
    
# Finding the null values in the dataset
dataset_null = df.isnull()
print(dataset_null)  

#number of null values in the dataset
print(df.isnull().sum())

#Finding the null values in particular column and find the number as well
dataset_null_column = df['order_id'].isnull()
print(dataset_null_column)

#for particular column
print(df['choice_description'].isnull().sum())

#percentage of null values in a dataset
percent_missing_dataset = df.isnull().mean()*100
print(percent_missing_dataset)

#percentage of null values in a column
percent_missing_quantity = df['choice_description'].isnull().mean()*100
print(percent_missing_quantity)


# list distinct entries of the 'col1' column
distinct_entries = df['choice_description'].unique()
print(distinct_entries)

# Lets check the unique item for these description to have more idea
distinct_entries =  df.loc[df['choice_description'].isnull(), 'item_name'].unique()
print(distinct_entries)

# Now we check how many unique item_name have null choice_description
count_distinct_entries= df[df['choice_description'].isnull()]['item_name'].nunique()
print("Number of unique item_name with null description:", count_distinct_entries)


# We can replace these missing values by 'Regular' or "no preferred choice".
#For the sake of continuity we choose Regular. 
df['choice_description'] = df['choice_description'].fillna('Regular Order')
print(df['choice_description'].head(10))

# Use boolean indexing to select the rows where choice_description is "Regular Order"
regular_orders = df[df['choice_description'] == 'Regular Order'].to_string(index=False)
# Display the selected rows
print(regular_orders)

#Let's check if we have null values or not. 
print(df.isnull().sum()) 


#Find the count of duplicate entries
count_duplicates = df[df.duplicated()].shape[0]
print("Number of duplicate rows:", count_duplicates)

#WE can verify by running following code:
duplicates = df[df.duplicated(keep=False)]
duplicates_sorted = duplicates.sort_values(by=['order_id'])
print(duplicates_sorted.to_string(index=False))

#delete the duplicate entries
df.drop_duplicates(inplace=True)

#lets check again
count_duplicates = df[df.duplicated()].shape[0]
print("Number of duplicate rows:", count_duplicates)

duplicates = df[df.duplicated(keep=False)]
duplicates_sorted = duplicates.sort_values(by=['order_id'])
print(duplicates_sorted.to_string(index=False))

#We successfully remove the duplicate entries. 

# Iterate through each column in the dataframe
for col in df.columns:
    # Check if the column is a string column
    if df[col].dtype == 'object':
        # Remove extra spaces from each string in the column
        df[col] = df[col].str.strip()



#This will print a frequency count of all unique values in the item_name column, 
# sorted in descending order. 
print(df['item_name'].value_counts())

'''This will print the value counts for each column in the DataFrame, 
with a blank line separating the output for each column.'''
for col in df.columns:
    print(f"{col}:")
    print(df[col].value_counts())
    print()


# describe the item_name that has maximu price
max_item = df.loc[df['item_price'] == max(df['item_price'])]
print(max_item)

#we can check unusual entry here.  since max_item price has max order quantity, 
# it makes sense and conclude that it has no error.

# export the modified data to a CSV file. 
df.to_csv('cleaned_data.csv', index=False)