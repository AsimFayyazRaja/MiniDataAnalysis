
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as plt


# In[23]:


data=[58.6462,243.018,0.99726968,1.02595676,0.41354,0.44401,0.71833,0.67125,6.3872]  #data set of orbital speed in Earth's days taken from NASA
np_orbitaldata=np.array(data)
print("The mean of the orbital speed: ",np.mean(np_orbitaldata))


# In[27]:


data1=[3.70,8.87,9.80,3.71,24.79,10.44,8.87,11.15,0.66]  #data set of gravity in ms^-2 taken from NASA
np_gravitydata=np.array(data1)
print(np_gravitydata)
print("The mean of the gravity: ",np.mean(np_gravitydata))


# In[35]:


xlab = 'Gravity'
ylab = 'Orbital Speed'
title = 'Relation b/w gravity and orbital speed'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.plot(np_gravitydata,np_orbitaldata)
plt.show()

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.scatter(np_gravitydata,np_orbitaldata,c="red",alpha=.8)
plt.show()


# In[30]:


plt.hist(data1,7)
plt.show()

