# Rolling a dice

# In this code, I want to roll a dice for n times and count the number of 6s


import numpy as np
import random

num=0 #number of 6s
n=60000 #number of rolling the dice
for n in range(0,n):
    
    r=np.random.choice(6, 1, p=[1/6, 1/6, 1/6, 1/6, 1/6,1/6])
    if r==5:
        num=num+1

print('num=',num);
