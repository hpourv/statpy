
# Flipping a coin

# In this code I want to flip a coin for n times and see the results


import numpy as np
import random

num_head=0 #number of head
num_tale=0 #number of tale
n=5 #number of flipping the coin
for n in range(0,n):
    
    r=np.random.choice(2, 1, p=[0.5, 0.5])
    if r==1:
        num_head=num_head+1
    else:
        num_tale=num_tale+1
print('num_head=',num_head,'num_tale=',num_tale);
