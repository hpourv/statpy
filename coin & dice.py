

# Flipping a coin

# In this section I want to flip a coin for n times and see the results


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


# Rolling a dice

# In this section, I want to roll a dice for n times and count the number of 6s


import numpy as np
import random

num=0 #number of 6s
n=60000 #number of rolling the dice
for n in range(0,n):
    
    r=np.random.choice(6, 1, p=[1/6, 1/6, 1/6, 1/6, 1/6,1/6])
    if r==5:
        num=num+1

print('num=',num);

