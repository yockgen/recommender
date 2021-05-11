#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[16]:


r_cols = ['user_id', 'prd_id','title', 'rating']
ratings = pd.read_csv('GAME1000.csv', sep=',', names=r_cols, usecols=range(4), encoding="ISO-8859-1",skiprows=1)
#ratings


# In[17]:


ratings =ratings.drop_duplicates()
#atings


# In[18]:


prdRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating',fill_value=0)
prdRatings.head()


# In[22]:


iRecurrence = 1
prdStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
popularPrdTmp = prdStats['rating']['size'] >= iRecurrence
popularPrd = prdStats[popularPrdTmp].sort_values([('rating', 'mean')], ascending=False)


# In[23]:


def recommendItem(sItemNm, dfPivotRating,dfPopularItems):
    
    inferenceRatings = dfPivotRating[sItemNm] 
    inferenceRatings.head()

    similarItems = dfPivotRating.corrwith(inferenceRatings,axis=0)
    similarItems = similarItems.dropna()
    similarItems = similarItems.sort_values(ascending=False)
    
    df = dfPopularItems.join(pd.DataFrame(similarItems, columns=['similarity']))
    df = df.sort_values(['similarity'], ascending=False)
    return df
   
    
#dfTmp = recommendItem("FF7",prdRatings,popularPrd)
#print(dfTmp.head())
  


# In[24]:



for col in prdRatings.columns: 
    print ("\nprd=",col)
    dfTmp = recommendItem(col,prdRatings,popularPrd)

    for idx, row in dfTmp.iterrows():         
       print(idx, row['similarity'],row[0])
    
 
    #print (dfTmp.head())


# In[ ]:




