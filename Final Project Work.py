#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
covid_data=pd.read_csv('https://data.chhs.ca.gov/dataset/e39edc8e-9db1-40a7-9e87-89169401c3f5/resource/de27ce58-edc8-45fb-bebc-08c4b29c5efe/download/covid19postvaxstatewidestats_07172022.csv%27')
covid_data.head(533)


# In[21]:


unv_cases = 'unvaccinated_cases'
v_cases = 'vaccinated_cases'
print(covid_data[unv_cases])
print(covid_data[v_cases])


# In[ ]:





# In[ ]:




