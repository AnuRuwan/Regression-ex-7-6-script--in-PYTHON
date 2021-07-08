#!/usr/bin/env python
# coding: utf-8

# ## **Importing modules / libraries**

# In[1]:


import pandas as pn
import matplotlib.pyplot as plt
import numpy as np


# ## **Reading the data frame**

# In[2]:


reg = pn.read_csv("regrex1.csv")
print(reg)


# ## **Plotting the scatterplot**

# In[3]:


reg.plot.scatter(x = 'x', y = 'y', title = "Scatter plot-python")
plt.savefig("scatteplot-from script-origin-py.png")

# ## **Linear modeling**

# In[4]:


xdata=reg['x']
ydata=reg['y']
plt.plot(xdata, ydata, 'o', color='blue')
m, b =np.polyfit(xdata, ydata, 1)
plt.plot(xdata,m*xdata+b)


# In[ ]:




