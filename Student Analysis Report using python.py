#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# calling dataset
df=pd.read_csv("student_scores.csv")
print(df.head()) #saare columns call ho jaty h using head


# In[3]:


df.describe() #columns jisme numeric value h 


# In[4]:


df.info()


# In[6]:


df.isnull().sum() #jisme null values present h


# In[8]:


# drop unnamed column
df=df.drop("Unnamed: 0",axis=1)
print(df.head())


# In[22]:


#gender distribution count
plt.figure(figsize=(5,5))
ax = sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0]) #to show the exact count
plt.title("Gender Distribution")
plt.show()


# In[ ]:


# from the above chart we have analyzed that no of females data is more than the no of males data


# In[13]:


# parents education impact on student scores
gb = df.groupby("ParentEduc").agg({"MathScore":'mean' , "ReadingScore":"mean", "WritingScore":"mean"})
print(gb)


# In[23]:


# using heatmap when we have one column of string values and other of numeric
# plt.figure(figsize=(1,1)) #for figure size
sns.heatmap(gb, annot=True)
plt.title("Relationship between Parent's Education and Student Scores")
plt.show()


# In[ ]:


# from above chart we have concluded that parents education have great impact on student scores


# In[27]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean' , "ReadingScore":"mean", "WritingScore":"mean"})
print(gb1)


# In[29]:


sns.heatmap(gb1, annot=True)
plt.title("Relationship between Parent's Martial Status and Student Scores")
plt.show()


# In[25]:


# from above chart we have concluded that parents martial status have not  much or neglagible impact on student scores


# In[30]:


#box plot tells us whether in our data outliers(extreme value) are there or not
sns.boxplot(data=df , x="MathScore")
plt.show()


# In[31]:


sns.boxplot(data=df , x="ReadingScore")
plt.show()


# In[32]:


sns.boxplot(data=df , x="WritingScore")
plt.show()


# In[33]:


print(df["EthnicGroup"].unique())


# In[35]:


#distribution of ethnic groups


groupA = df.loc[(df['EthnicGroup']=="group A")].count()
print(groupA)


# In[46]:


groupB = df.loc[(df['EthnicGroup']=="group B")].count()
groupC = df.loc[(df['EthnicGroup']=="group C")].count()
groupD = df.loc[(df['EthnicGroup']=="group D")].count()
groupE = df.loc[(df['EthnicGroup']=="group E")].count()


l = ["groupA", "groupB", "groupC","groupD","groupE"]
mlist=[groupA["EthnicGroup"] ,groupB["EthnicGroup"], groupC["EthnicGroup"],groupD["EthnicGroup"] , groupE["EthnicGroup"]]
print(mlist)
plt.pie(mlist, labels = l, autopct= "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[47]:


ax = sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0]) #to show the exact count
plt.show()


# In[ ]:




