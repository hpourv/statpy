# In this code I trying to visualize the realization of law of larg numbers.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import random
N=10000; 
a=np.zeros(N);
for i in range(N):
   h=np.random.uniform(1.4,2.1,[1,1000])
   a[i]=np.mean(h)
sns.displot(a)  
