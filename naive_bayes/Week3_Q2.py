
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Q2-tennis.csv')


# In[7]:


# Calculate count of each word.
c_yes = df[df['Play'] == 'yes'].count()['Play']
c_sunny = df[df['Outlook']=='sunny'][ df['Play'] == 'yes'].count()['Outlook']
c_overcast = df[df['Outlook']=='overcast'][ df['Play'] == 'yes'].count()['Outlook']
c_rainy = df[df['Outlook']=='rainy'][ df['Play'] == 'yes'].count()['Outlook']
c_hot = df[df['Temp.']=='hot'][ df['Play'] == 'yes'].count()['Temp.']
c_mild = df[df['Temp.']=='mild'][ df['Play'] == 'yes'].count()['Temp.']
c_cold = df[df['Temp.']=='cold'][ df['Play'] == 'yes'].count()['Temp.']
c_high = df[df['Humidity']=='high'][ df['Play'] == 'yes'].count()['Humidity']
c_normal = df[df['Humidity']=='normal'][ df['Play'] == 'yes'].count()['Humidity']
c_windT = df[df['Windy']=='true'][ df['Play'] == 'yes'].count()['Windy']
c_windF = df[df['Windy']=='false'][ df['Play'] == 'yes'].count()['Windy']


# In[17]:


#calculating probabilities when Play is True
p_yes = c_yes/df['Play'].count()
p_Ysunny = c_sunny/c_yes
p_Yovercast = c_overcast/c_yes
p_Yrainy = c_rainy/c_yes
p_Yhot = c_hot/c_yes
p_Ymild = c_mild/c_yes
p_Ycold = c_cold/c_yes
p_Yhigh = c_high/c_yes
p_Ynormal = c_normal/c_yes
p_YwindT = c_windT/c_yes
p_YwindF = c_windF/c_yes


# In[18]:


#Probability of each word
p_sunny = df[df['Outlook']=='sunny'].count()['Outlook']/df['Outlook'].count()
p_overcast = df[df['Outlook']=='overcast'].count()['Outlook']/df['Outlook'].count()
p_rainy = df[df['Outlook']=='rainy'].count()['Outlook']/df['Outlook'].count()
p_hot = df[df['Temp.']=='hot'].count()['Temp.']/df['Temp.'].count()
p_mild = df[df['Temp.']=='mild'].count()['Temp.']/df['Temp.'].count()
p_cold = df[df['Temp.']=='cold'].count()['Temp.']/df['Temp.'].count()
p_high = df[df['Humidity']=='high'].count()['Humidity'] / df['Humidity'].count()
p_normal = df[df['Humidity']=='normal'].count()['Humidity'] / df['Humidity'].count()
p_windT = df[df['Windy']=='true'].count()['Windy'] / df['Windy'].count()
p_windF = df[df['Windy']=='false'].count()['Windy'] / df['Windy'].count()


# In[22]:


def PcalY(look, temp, humd, wind):
    return (look*temp*humd*wind*p_yes)


# In[23]:


def PcalN(look, temp, humd, wind):
    return 1 - PcalY(look, temp, humd, wind)


# In[27]:


print(PcalY(p_Ysunny, p_Yhot, p_Yhigh, p_YwindF))


# In[28]:


# Laplacian Correction
c_yes += 10
p_Ysunny = c_sunny+1/c_yes
p_Yovercast = c_overcast+1/c_yes
p_Yrainy = c_rainy+1/c_yes
p_Yhot = c_hot+1/c_yes
p_Ymild = c_mild+1/c_yes
p_Ycold = c_cold+1/c_yes
p_Yhigh = c_high+1/c_yes
p_Ynormal = c_normal+1/c_yes
p_YwindT = c_windT+1/c_yes
p_YwindF = c_windF+1/c_yes


# In[29]:


print(PcalY(p_Ysunny, p_Yhot, p_Yhigh, p_YwindF))


# In[ ]:




