import numpy as np

var=np.array([1,2,3,4,5,6,5,4,3,2,1])

print(f"{np.sqrt(var)}\nmax:{np.max(var)}, min:{np.min(var)}, position: formin:{np.argmin(var)}, formax{np.argmax(var)}")

var1=np.array([[2,1,4],[9,8,3]])
print(f"max:{np.max(var1,axis=0)}, min:{np.min(var1,axis=0)}, position: formin:{np.argmin(var1)}, formax{np.argmax(var1)}")



var2=np.array([1,2,3,4])

print(np.sin(var2))
print(np.cos(var2))
print(np.cumsum(var2))