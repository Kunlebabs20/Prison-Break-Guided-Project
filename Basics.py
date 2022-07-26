#!/usr/bin/env python
# coding: utf-8

# # My First Data Science Project

# ## Dataquest Guided Project

# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# ## Helicopter Escapes!

# We begin by importing some helper functions

# In[119]:


from helper import *


# We are importing the url containing the list

# In[120]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'


# In[121]:


data = data_from_url(url)

for row in data:
    print(row)


# In[122]:


index = 0

for row in data:
    data[index] = row[:-1]
    index += 1


# In[123]:


print(data[:3])


# In[124]:


for row in data:
    row[0] = fetch_year(row[0])


# In[125]:


print(data[:3])


# In[132]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[133]:


print(min_year)
print(max_year)


# In[135]:


attempts_per_year = []
for y in years:
    attempts_per_year.append([y, 0])


# In[136]:


print(years)


# In[137]:


attempts_per_year = []
for y in years:
    attempts_per_year.append([y, 0]) 


# In[139]:


print(attempts_per_year)


# In[141]:



for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
            
print(attempts_per_year)    


# Visualizing the Years with most attempts at breaking out of prison with a Helicopter

# In[142]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[145]:



countries_frequency = df["Country"].value_counts()


# In[147]:


print_pretty_table(countries_frequency)

