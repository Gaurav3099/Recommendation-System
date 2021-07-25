#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data1 = pd.read_csv('movie_metadata.csv')


# In[3]:


df = data1[['movie_title','director_name','actor_1_name','actor_2_name','actor_3_name','genres','title_year']]
df.head()


# In[4]:


df['genres'] = df['genres'].apply(lambda a: str(a).replace('|', ' '))
df['movie_title'] = df['movie_title'].str.lower()
df['director_name'] = df['director_name'].str.lower()
df['actor_1_name'] = df['actor_1_name'].str.lower()
df['actor_2_name'] = df['actor_2_name'].str.lower()
df['actor_3_name'] = df['actor_3_name'].str.lower()
df['genres'] = df['genres'].str.lower()
df.head()


# In[5]:


df['movie_title'] = df['movie_title'].apply(lambda a:a[:-1])


# In[6]:


df['dgr'] = df['director_name']+df['actor_1_name']+df['actor_2_name']+df['actor_3_name']+df['genres']


# In[7]:


df.fillna('', inplace=True)


# In[8]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer()
cv_matrix = cv.fit_transform(df['dgr'])
similarity = cosine_similarity(cv_matrix)


# In[9]:


def rec_movie(movie):
#     f = df['movie_title'].str.contains(movie, na=False, case=False)
    op="Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies"
    movie=movie.lower()
    if movie not in df['movie_title'].unique():
#         print("Sorry! movie not in database")
        return op,op

    else:
        m = df.loc[df['movie_title']==movie].index[0]
        lst = list(enumerate(similarity[m]))
        lst = sorted(lst, key=lambda x:x[1], reverse = True)
        lst = lst[1:11]
        l = []
        year = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(df['movie_title'][a])
            year.append(df['title_year'][a])
        df1 = pd.DataFrame({'Movie Reommended':l, 'Year': year})
        return l,year
#         return df1


# In[10]:


#rec_movie("Inception")


# In[ ]:




