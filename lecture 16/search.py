import numpy as np

var=np.array([1,2,3,4,5,6,4,4,7,99,8])

x=np.where(var==4)
x=np.where(var/3==0)
x=np.where(var%2==0)
print(x)

var=np.array([1,2,3,4,6])

# x=np.searchsorted(var,5,side='right')
x=np.searchsorted(var,[5,6,7],side='right')
print(x)