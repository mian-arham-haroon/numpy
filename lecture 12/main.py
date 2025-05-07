import numpy as np

var=np.array([1,2,3,4,5,6,7])

print("2 to 5: ",var[1:4])
print("2 to end: ",var[1:])
print("starting to 5: ",var[:4])
print("stop: ",var[::2])

var1=np.array([[1,2,3,4,5],[9,8,7,6,5]])
print(var1[0,1:])
