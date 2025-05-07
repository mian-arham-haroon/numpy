import numpy as np

var0=np.array([1,2,5,6,7,8])

ar=np.array_split(var0,3)
print(ar)
print(ar[0])

var1=np.array([[1,2],[5,6],[7,8]])

ar=np.array_split(var1,3,axis=1)
print(ar)
print(ar[0])
