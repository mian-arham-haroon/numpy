from numpy import *
import numpy as np


# var1 = np.array([1,2,3,4,5,6])
# np.random.shuffle(var1)
# print(var1)

# var1 = np.array([1,2,3,4,3,2,1,3,4,5,6,4,2,5,6])
# x=np.unique(var1,return_index=True,return_counts=True)
# print(x)

# var1 = np.array([1,2,3,4,5,6])
# x=np.resize(var1,(2,3))
# print(x)

var1 = np.array([1,2,3,4,5,6])
x=np.resize(var1,(2,3))
print("flatten ",x.flatten(order='F'))
print("ravel ",np.ravel(x,order='C'))











