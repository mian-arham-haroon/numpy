import numpy as np

var=np.array([[1,2],[3,4]])
vara=np.array([[1,2],[3,4]])
# print(var+vara)
# print(var-vara)
# print(var*vara)
var1=np.matrix([[1,2],[3,4]])
var1m=np.matrix([[1,2],[3,4]])
# print(var1+var1m)
# print(var1-var1m)
# print(var1*var1m)
print(var1.dot(var1m))
print(type(var))
print(type(var1))









