#arithmentic operation
import numpy as np
#-----------------------------------------------------#
var=np.array([1,2,3,4])
varadd=var+3            #same for sub
print(varadd)
var=np.array([1,2,3,4])
var2=np.array([4,5,6,7])
varadd1=var-var2            #sam for sum
print(varadd1)
#-----------------------------------------------------#
var=np.array([1,2,3,4])
varadd=var*3            
print(varadd)
var=np.array([1,2,3,4])
var2=np.array([4,5,6,7])
varadd1=var*var2            
print(varadd1)
#-----------------------------------------------------#
var=np.array([1,2,3,4])
varadd=var/3            
print(varadd)
var=np.array([1,2,3,4])
var2=np.array([4,5,6,7])
varadd1=var/var2            
print(varadd1)
#-----------------------------------------------------#
var=np.array([1,2,3,4])
varadd=var%3            
print(varadd)
var=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd1=var%var2            
print(varadd1)

#-----------------------------------------------------#
var=np.array([1,2,3,4])
varadd=np.mod(var,var2)            #we all use the function
print(varadd)
var=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd1=var%var2            
print(varadd1)
var3=np.array([[1,2,3,4],
             [4,5,6,7]])
var4=np.array([[1,2,3,4],
              [4,5,6,8]])
varadd=np.multiply(var3,var4)            #we all use the function all 2d
print(varadd)

var=np.array([1,2,3,4])
varadd=np.reciprocal(var)            
print(varadd)
