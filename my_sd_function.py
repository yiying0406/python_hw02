
# coding: utf-8

# In[1]:

#using Python to write standard diviation formation by 陳怡穎
import math
import numpy as np
def sd(mylist):
    n = len(mylist)
    mu = np.mean(mylist)
    sigma =np.sum((mylist-mu)*(mylist-mu))
    sqrt = math.sqrt((1/n) * sigma)
    return sqrt
# mylist= (5,6,8,9) :1.5811388300841898
mylist = range(1,11) #2.8722813232690143
print(sd(mylist))


# In[ ]:



