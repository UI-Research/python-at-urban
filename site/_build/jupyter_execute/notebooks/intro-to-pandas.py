#!/usr/bin/env python
# coding: utf-8

# # Intro to Pandas

# While built-in Python functions suffice for general programming, data analysis requires additional functions and objects. Pandas is a popular data analysis package that is simple to use the moment you start Python.
# 
# The primary reason Pandas is popular for data science and analysis is that it introduces three useful objects that mirror similar data structures from other statistical packages and don't add complexity to the simple Pythonic syntax. These objects are:
# 
# 1. The DataFrame
# 2. The Series
# 3. The Index
# 
# This guide is not meant to be comprehensive, the most comprehensive documentation for Pandas is found [here](https://pandas.pydata.org/docs/#). The purpose of this guide is to inform a potential user of the functionality of Pandas and a general overview of how to accomplish basic data analysis tools.

# ## Getting Started
# 
# ### Importing Pandas
# Since Pandas is not native to Python, you will have to install it. Fortunately, Pandas has grown so much in popularity, that most downloads (including Anaconda) will contain Pandas, but you will still have to load the package. This code will do the trick:

# In[1]:


import pandas 


# However, because Pandas is used so often, the Python community loads pandas as `pd` for ease of access: 

# In[2]:


import pandas as pd


# It's also useful to import a few other packages, mostly notably Numpy.

# In[3]:


import numpy as np


# ### DataFrame

# The DataFrame object is one of the main contributions of Pandas. The DataFrame is a 2-dimensional labeled structure with columns and rows. The columns and the rows represent one dimension each. The DataFrame is analogous to the R and Stata DataFrame and the Excel spreadsheet. Or put in more technical terms, the DataFrame is a tabular data structure. The code below defines a DataFrame and then prints it out to view:

# In[4]:


d = pd.DataFrame({'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]})

d


# `d` is the name of our DataFrame and it has two columns, one and two, and four rows, 0-3. (Python is 0 indexed, meaning it counts from 0...1...2...and so on.)
# 
# Each data point can be referenced through its Index (which corresponds to its row, the far most left value) and the column signifies what the value means. We can call a single Pandas column with this command:

# In[5]:


(d['one'])


# The values on the left represent the Index we saw earlier. Notice: A column's type is itself a Pandas object, the Series. More on this object below.
# 
# 

# ### Series
# A Series is one-dimensional indexed array that can contain any Python data type. To create a Series you use the function: 

# In[6]:


series_ex = pd.Series([1,2,3,4])


#  A Series in Pandas is similar visually to a list. But there are key distinctions in how they opearte. As mentioned, Pandas is used for data analysis, so a Series has functions that allow for data analysis to be done easily, while a list would require either a for loop or list comprehension for the same operations. Example of this below:

# In[7]:


series_ex = series_ex*2
print("This is a Series multipled by two")
print(series_ex)


# In[8]:


list = [1,2,3,4]
list = list*2
print("This is a List multipled by two")
print(list)


# ### Index
# 
# Both the Series and the DataFrame have an index that signifies order and allows for referencing specific points. The Index itself is an object - though by itself it holds little purpose. 

# In[9]:


ind = pd.Index([2, 3, 5, 7, 11])
ind


# ## Importing Data

# Pandas has the ability to read and export multiple data format types: be it a csv, dta, sas file, json file, sql and many more. Almost all data reading will be in the format: 
# 
# `pd.read_(NAME OF DATA FORMAT)('FILE_NAME')` 
# 
# Let's take a look at a few examples. 

# ### Stata Files (DTA)

# In[10]:


# Importing data from Stata 
pd.read_stata('data/State_ETO_short.dta')


# This is how we read in a DataFrame, but we still need to store and name it. This can be accomplished in one line:

# In[11]:


df = pd.read_stata('data/State_ETO_short.dta')


# Now, when we call `df`, we'll get the DataFrame that corresponds to the data referenced in `pd.read_stata('data/State_ETO.dta')`. 

# In[12]:


df


# ### Excel Files (XLSX)

# In[13]:


# Importing data from excel into pandas
df = pd.read_excel('data/Minimum_Wage_Data_Short.xlsx')
df


# ### Other Data Types
# Similar variants for uploading exists for each common data type - CSV, SAS, and so on.

# ## Exporting Data
# 
# Exporting data is very simple as well and follow a pattern similar to exporting.

# ### CSV

# In[14]:


df.to_csv('exports/Minimum_Wage_Data.csv')


# ## Converting Data

# Now that we know how to load in data, it will be useful to examine ways to convert already existing data structures into DataFrames. 

# ### List

# In[15]:


my_list = [1,2,3,4,5,6,7,8,9]
columns = ['a', 'b', 'c']

pd.DataFrame(np.array(my_list).reshape(3,3), columns = columns)


# An important thing to note: `pd.DataFrame` has a multitude of options. The most import of which is what follows right after the first parentheses which is the data that is to be transformed. Here are transform the list `[1,2,3,4,5,6,7,7,8,9]` into an `np.array` with the shape of: 
# 
#     [[1,2,3],
#     [4,5,6], 
#     [7.8.9]]
#     
# Then we transform the data to a Pandas DataFrame which gives us: 
# 
#     0	1	2	3
#     1	4	5	6
#     2	7	8	9
#     
#     
# Finally, we add a list of column name with the option `columns = columns` to get the final dataframe.
# 
# 
#     	a	b	c
#     1	4	5	6
#     2	7	8	9
# 

# ### Dictionary

# In[16]:


data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)


# ### Numpy Array

# In[17]:


dtype = [('Col1','int32'), ('Col2','float32'), ('Col3','float32')]
values = np.zeros(5, dtype=dtype)
index = ['Row'+str(i) for i in range(1, len(values)+1)]

pd.DataFrame(values, index=index).head()


# Now that we know how to load in our DataFrame, we will try to view and manipulate our data before our analysis is run. 

# ## Viewing Data 

# We know that we can view our data by simply printing the dataframe, but what if our data is too large?
# 
# The `.head()` function prints out the first 5 rows. (inside the parentheticals you can specify the first N observations you want to see).

# In[18]:


df.head()


# In[19]:


df.head(2)


# You can also do all of these methods on a single Series. 

# In[20]:


df['Year'].head()


# Or, you can do multiple columns at one time. 

# In[21]:


df[['State', 'Table_Data']].head()


# It's also good to view general information on the dataframe from `.info()` and to understand the datatypes of each of the columns. 

# In[22]:


df.info()


# In[23]:


df.dtypes


# Similar to our use of `head()`, we can use `tail()` to examine the last few data points. 

# In[24]:


df.tail(2)


# ## Subsetting Data

# We can do traditional slicing through the index `[start, end]`. This will subset by rows. 
# 
# We can also do subsetting by the series `df[['columns_we_want_1', 'columns_we_want_2']]`. This will subset by columns.

# Slicing by the index is similar to slicing any Python object by its index.

# ### Slicing the data by rows

# In[25]:


df[1:4]


# ### Slicing the data by columns

# In[26]:


columns_you_want = ['State', 'Table_Data'] 
df[columns_you_want].head()


# Let's bring in a larger dataset for this analysis to be meaningful. This will be a panel dataset of states, so there will be 50 rows for every year 

# In[27]:


df = pd.read_excel("data/Minimum_Wage_Data.xlsx")


# In[28]:


print("This is the first five observations \n")
print(df[['Year', 'State']].head(5))
print("\n")

print("This is the last five observations \n")
print(df[['Year', 'State']].tail(5))


# Viewing the size and columns of the data:

# In[29]:


print(len(df))
print(df.columns)


# We have 8 variables: `Year`, `State`, `Table_Data`, `High_Value`, `Low_Value`, `CPI_Average`, `High_2018`, and `Low_2018`. Sometimes in our analysis we only want to keep certain years. For this, the traditional boolean logic mixed with Pandas slices the data into the segments we want.

# ### Slicing based on conditions

# In[30]:


# Rows past 2015
print(df[df.Year > 2015].head(3))


# Segmenting on multiple conditions is also desirable. Most programs allow for an "AND" operator and an "OR" operator.

# In[31]:


# California AND 2010
print(df[(df.Year == 2010) & (df.State == 'California')].head(3))
print('\n')


# In[32]:


# Alabama OR before 2015
print(df[(df.State == "Alabama") | (df.Year < 2015)].head(3))


# The traditional Python index slicers are also applicable for DataFrames with the `.loc[]` method.

# In[33]:


print(df.iloc[99])
print('\n')
print(df.iloc[[1, 50, 300]])


# In[34]:


print(df.loc[100])
print('\n')
print(df.loc[[2, 51, 301]])


# ## Summary Statistics
# Often times, exporting summary stats in a different document type is the best way to visualize the results and understand the data.

# In[35]:


df.describe()
print(df.describe())
np.round(df.describe(), 2)
np.round(df.describe(), 2).T
df.describe().transpose().to_csv('exports/summary_stats.csv', sep=',')


# ## Manipulating Data

# The standard way to create a new Pandas column or replace an old one is to call the Series (whether it exists or not) on the left hand side and set it equal to the expression that expresses that value you want to create. For example:
# 
# 

# ### Creating a new variable

# In[36]:


df['7'] = 7
print(df.head())


# Or, we can replace an old variable in a similar way. 

# ### Replacing a variable

# In[37]:


df['7'] = 8
print(df.head())


# We can also rename variables. In this case we will rename `Year` to `Date` and `Table_Data` to `Values.`

# ### Renaming Variables

# In[38]:


print(df.head())
print("\n")
print(df.rename(index=str, columns={"Year": "Date", "Table_Data": "Values"}).head())


# ### Dropping Variables
# We can also drop a variable with `df.drop()`: 

# In[39]:


# Dropping a variable
df = df.drop("7", axis=1)
print(df.head())


# Basic math operations are also easily applied in Pandas. 

# In[40]:


df['Difference'] = df['High_Value'] - df['Low_Value']
df['High*2'] = df['High_Value']*2
df['Low*2'] = df['Low_Value']*2
print(df.head())


# ### Complex Variable Modification with `.map()`
# 
# More complex operations can be solved through the `.map()` method. 
# 
# In the example below, `.map()` uses a dictionary to change results, which can help keep your code clean when replacing a large amount of values. Here we create an `abbrev` column for state abbreviations (we will create it and drop the variable after). 

# In[41]:


# Using Data.map
state_2 = {'OH': 'Ohio', 'Illinois': 'IL', 'California': 'CA', 'Texas': 'TX'}

df['abbrev'] = df['State'].map(state_2)


# In[42]:


df.sort_values('abbrev', ascending=True).head()
df = df.drop("abbrev", axis=1)


# ### Using Functions
# 
# You can use `.apply()` to apply a function to a Series. You can either specify the function or use the lambda anonymous function:

# Specfying a function:
# 

# In[43]:


def add(x):
    x = x + 1
    return x

print(df['Year'].head())
print("\n")
print(df['Year'].apply(add).head())


# #### Lambda Functions
# Lambda Functions (skipping defining a function if the function is simple enough):

# In[44]:


print(df['Year'].head())
print("\n")
print((df['Year'].apply(lambda x: x + 1).head()))


# ### Missing Values

# Dealing with missing values is an important part of data cleaning and something to always be mindful of. Pandas codes missing values as numpy `NaN` values. 

# In[45]:


print(df['Table_Data'].head(10))
print("\n")
print(df['Year'].head(10))


# Discovering missing values is  important: 

# In[46]:


print(df['Table_Data'].isnull().values.any())
print(df['Year'].isnull().values.any())


# We can also use `.drop_duplicates(keep = "first")` to drop all but the first observations of duplicates.
# 
# 

# In[47]:


data = {'col_1': [3, 3, 3, 3], 'col_2': ['a', 'a', 'a', 'a']}
data_dup = pd.DataFrame.from_dict(data)
print(data_dup)

print("\n")

data_dup = data_dup.drop_duplicates(keep="last")

print(data_dup)


# ## Reshaping Data
# 
# Data can be reshaped using a variety of Pandas functions. Going from wide to long has a built in function `wide_to_long()`. We will load in a new dataset for this:

# In[48]:


df_ex = pd.DataFrame({
    'Unique Family Identifier': [1000, 1000, 1000, 1001, 1001, 1001, 1002, 324, 234],
    'Order': [1, 2, 3, 1, 2, 3, 1, 2, 3], 
    'az1': [28, 82, 23, 234, 234, 324, 546, 546, 5464],
    'az2': [2342, 2342, 54645, 56765, 65765, 65756, 3453, 56756, 3453]})


reshape = pd.wide_to_long(df_ex, stubnames='az', i=['Unique Family Identifier', 'Order'], j='age')

print(df_ex.head())
print("\n")
print(reshape)


# Going from wide to long requires the use of `unstack()`. 

# In[49]:


normal = reshape.unstack()
normal.columns = normal.columns.map('{0[0]}{0[1]}'.format)
normal.reset_index()
print(normal.head())


# ## Merging Data
# 
# Merging data uses `pd.merge(data_1, data_2, on = identifier)`. 

# In[50]:


left_frame = pd.DataFrame({'key': range(5), 
                           'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7), 
                           'right_value': ['f', 'g', 'h', 'i', 'j']})
print(left_frame)
print('\n')
print(right_frame)


# In[51]:


pd.merge(left_frame, right_frame, on='key', how='inner')


# In[52]:


pd.merge(left_frame, right_frame, on='key', how='left')


# In[53]:


pd.merge(left_frame, right_frame, on='key', how='right')


# ## Appending Data

# In[54]:


pd.concat([left_frame, right_frame], sort='True')


# ## Collapsing Data

# Collapsing data is accomplished by the `.groupby()` function. We will collapse by `Year`. 

# In[55]:


by_year = df.groupby('Year')
print(by_year.count().head()) # NOT NULL records within each column


# Note: This only generates counts for each year. If we want averages, sums or any other summary statistics we have to specify that: 

# In[56]:


print(by_year.sum()[20:25])
print('\n')
print(by_year.mean()[20:25]) 
print('\n')
print(by_year.median()[20:25]) 


# 
