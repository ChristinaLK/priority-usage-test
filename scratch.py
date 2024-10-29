#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


datafile = "exports/2024-10-20_7days_priojobs.csv"


# In[9]:


data = pd.read_csv(datafile)


# In[12]:


data_select = data[["Owner","ProjectName","RequestCpus","RequestGpus","RemoteWallClockTime","PrioNodes"]]


# In[35]:


## generate user-centric summary

data_users = data_select.groupby(["Owner","ProjectName"]).aggregate({'RequestCpus' : ['mean'], 
                                                        'RemoteWallClockTime' : ['sum'],
                                                        'PrioNodes':['count','unique']
                                                       }).sort_values(['ProjectName','Owner'])
#dat.columns = dat.columns.to_flat_index()
data_users.columns = data_users.columns.to_flat_index()


# In[36]:


users_file = "exports/2024-10-20_7days_priojobs_user.csv"
data_users.to_csv(users_file)


# In[37]:


# generate node-centric summary

data_nodes = data_select.groupby(["PrioNodes"]).aggregate({'RemoteWallClockTime' : ['sum'], 
                                                           'Owner':['count','unique'],
                                                           'ProjectName':['count','unique']
                                                       }).sort_values('PrioNodes')
#dat.columns = dat.columns.to_flat_index()
data_nodes.columns = data_nodes.columns.to_flat_index()


# In[38]:


nodes_file = "exports/2024-10-20_7days_priojobs_node.csv"
data_nodes.to_csv(nodes_file)


# In[ ]:





# In[ ]:




