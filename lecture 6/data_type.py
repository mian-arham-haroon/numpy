#data type
import numpy as np
#--------------------------------------------#
var=np.array([1,2,3,4,5])
print("data type",var.dtype)
#--------------------------------------------#
var2=np.array([1.0,2.0,3.0,4.0,5.0])
print("data type",var2.dtype)
#--------------------------------------------#
var3=np.array(["a","b"])
print("data type",var3.dtype)
#--------------------------------------------#
var4=np.array(["a","b",1,2])
print("data type",var4.dtype)
#--------------------------------------------#
var5=np.array([1,2,3,4,5],dtype=np.int8)
print("data type",var5.dtype)
print(var5)
#--------------------------------------------#
var6=np.array([1,2,3,4,5],dtype="f")
print("data type",var6.dtype)
print(var6)
#--------------------------------------------#
var7=np.array([1,2,3,4,5])
new=np.float32(var7)
print("data type",var7.dtype)
print(var7)
print("data type",new.dtype)
print(new)
#--------------------------------------------#
var8=np.array([1,2,3,4,5])
new=np.float32(var8)
new1=np.int_(new)
print("data type",var8.dtype)
print(var8)
print("data type",new.dtype)
print(new)
print("data type",new1.dtype)
print(new1)
#--------------------------------------------#
var9=np.array([1,2,3,4,5])

new_1=var9.astype(float)

print(var9)
print(new_1)
#--------------------------------------------#