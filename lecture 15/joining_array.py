import numpy as np

var=np.array([1,2,3,4])
var2=np.array([5,6,7,8])

ar=np.concatenate((var,var2))

print(ar)

var3=np.array([[1,2,3,4],[11,12,13,14]])
var4=np.array([[5,6,7,8],[21,22,23,24]])

ar1=np.concatenate((var3,var4),axis=1)

print(ar1)
#stack
var=np.array([1,2,3,4])
var2=np.array([5,6,7,8])

ar=np.stack((var,var2),axis=1)

print(ar)

ar=np.hstack((var,var2))

print(ar)

ar=np.vstack((var,var2))

print(ar)

ar=np.dstack((var,var2))

print(ar)





