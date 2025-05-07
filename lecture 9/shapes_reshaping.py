#shapes
import numpy as np
#-------------------------------------------------------#
var=np.array([[1,2],[1,2]])

print(var.shape)
#-------------------------------------------------------#
var1=np.array([1,2,4,4,5,6],ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)
#-------------------------------------------------------#
var3=np.array([1,2,3,4,5,6])
x=var3.reshape(2,3)
print(x)
print(x.ndim)
print(x.shape)

#-------------------------------------------------------#
var5=np.array([1,2,4,4,5,6,7,8,9,10,11,12])
print(var5)
x1=var5.reshape(2,3,2)
print(x1)
print(x1.ndim)
print(x1.shape)
one=x1.reshape(-1)
print(one)
print(one.ndim)
#-------------------------------------------------------#