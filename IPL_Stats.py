#!/usr/bin/env python
# coding: utf-8

# THIS Code Aims to create a batter against bowler data visual for all ballers and batters in IPL 2023 till matchday 23
# 
# It will be extended to analysis for prediction for players

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("combined_csv.csv")


# In[3]:


df.info()


# In[4]:


# Replace 'w' with 12 and remove all other letters
df['outcome'] = df['outcome'].replace({'w': 12, 'wd': 0}, regex=True).map(lambda x: int(''.join(filter(str.isdigit, str(x)))))

print(df)


# In[5]:


# Drop rows where batter is 'n Sundar'
df = df.drop(df[df['batter'] == 'n Sundar'].index)

print(df)


# In[6]:


# Filter the data where outcome is not 12
filtered_data = df[df['outcome'] != 12]

# Group the data by batter and bowler and calculate the sum of outcomes
sum_outcomes = filtered_data.groupby(['batter', 'bowler'])['outcome'].sum()

print(sum_outcomes)


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


def bowlerstate(x):
    filtered_data = df[(df['outcome'] != 12) & (df['bowler'] == x)]

    # Group the data by batter and calculate the sum of outcomes
    sum_outcomes = filtered_data.groupby('batter')['outcome'].sum()

    # Create a bar chart of the sum of outcomes for each batter
    sum_outcomes.plot(kind='bar')

    # Set the title and axis labels
    plt.title('Outcomes for '+x.capitalize()+' against All Batters')
    plt.xlabel('Batter')
    plt.ylabel('Sum of Outcomes (excluding wickets)')

    # Display the chart
    plt.show()


# In[9]:


x = input("bowler name")
bowlerstate(x)


# In[10]:


def batterstate(x):
    filtered_data = df[(df['outcome'] != 12) & (df['batter'] == x)]

    # Group the data by batter and calculate the sum of outcomes
    sum_outcomes = filtered_data.groupby('bowler')['outcome'].sum()

    # Create a bar chart of the sum of outcomes for each batter
    sum_outcomes.plot(kind='bar')

    # Set the title and axis labels
    plt.title('Outcomes for'+x.capitalize()+'against All Bowlers')
    plt.xlabel('Bowler')
    plt.ylabel('Sum of Outcomes (excluding wickets)')

    # Display the chart
    plt.show()


# In[11]:


y = input("batter name")
batterstate(y)


# In[ ]:




