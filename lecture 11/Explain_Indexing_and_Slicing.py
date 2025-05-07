import numpy as np



var=np.array([1,3,4,5,7,8])

print(var[1])       #postive indexing
print(var[-3])

var1=np.array([[1,3,4,5,7,8],[2,4,5,8,7,8]])
print(var1)
print()
print(var1.ndim)
print()
print(var1[0,1])

var2=np.array([[[1,3,4,5,7,8],[2,4,5,8,7,8]]])
print(var2)
print()
print(var2.ndim)
print()
print(var2[0,0,3])





























