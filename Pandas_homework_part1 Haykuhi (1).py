#!/usr/bin/env python
# coding: utf-8

# ## Importing pandas
# 
# **1.** Import pandas under the name `pd`.
# 
# Import արեք pandas մոդուլը `pd` անունով։

# In[44]:


import pandas as pd


# **2.** Print the version of pandas that has been imported.
# 
#  Տպեք pandas մոդուլի տարբերակը։

# In[2]:


pd.__version__


# ## DataFrame basics
# 
# 
# 
# Consider the following Python dictionary `data` and Python list `labels`:
# 
# 
# 

# In[66]:


import numpy as np



data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# **3.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.
# 
# Ստեղծեք `df` DataFrame `data` dictionary-ից, որի index-ը կլինի `labels` list-ը։

# In[67]:


df = pd.DataFrame(data, index = labels)
df


# **4.** Return the first 3 rows of the DataFrame `df`.
# 
# Տպեք `df` DataFrame-ի առաջին 3 տողերը։

# In[68]:


df[:3]


# **5.** Select just the `animal` and `age` columns from the DataFrame `df`.
# 
# `df` DataFrame-ից ընտրեք միայն `animal` և `age` սյուները։

# In[69]:


df[["animal","age"]]


# **6.** Select the data in rows `[3, 4, 8]` and in columns `['animal', 'age']`.
# 
# `df`-ից վերցրեք `[3, 4, 8]` տողերում ու `['animal', 'age']` սյուներում գտնվեղ տվյալները։

# In[70]:


df.loc[df.index[[2, 3, 7]],["animal" , "age"]]


# **7.** Select only the rows where the number of visits is greater than 3.
# 
# Ընտրեք `df` DataFrame-ի այն տողերը, որոնց տվյալների համար visits սյան արժեքը 3-ից մեծ է։

# In[71]:


df[df["visits"] > 3]


# **8.** Select the rows where the age is missing, i.e. is `NaN`.
# 
# Ընտրեք այն տողերը, որոնց տվյալների համար age սյունի արժեքը բացակայում է՝ այսինքն `NaN` է։

# In[88]:


df[(df["age"] == np.NaN)]


# **9.** Select the rows where the animal is a cat and the age is less than 3.
# 
# Ընտրեք այն տողերը, որոնց տվյալների համար animal սյունի արժեքը cat է և age սյունի արժեքը փոքր է 3-ից։

# In[86]:


df[(df['age']<3) & (df['animal'] == "cat")]


# **10.** Change the age in row 'f' to 1.5.
# 
# Փոխարինեք 'f' տողի age սյունի արժեքը 1.5-ով։

# In[92]:


df["age"]["f"] = 1.5
df


# **11.** Add a new column 'n' with all 1s.
# 
# Ավելացրեք միայն 1-եր պարունակող 'n' սյունը։

# In[96]:


df["n"] = 1
df


# **12.** Count the number of each type of animal in `df`.
# 
# Հաշվեք `df`-ում տեղ գտած կենդանիների տիպերի քանակը։

# In[101]:


x = df['animal'].value_counts()
x

