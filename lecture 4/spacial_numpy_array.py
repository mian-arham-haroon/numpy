import numpy as np
#zero array

ar_zero=np.zeros(4)         #one d array 
ar_zero1=np.zeros((3,4))    #it is use for the 2 d array
# d2=np.array([[3,4],[3,4]])
# print(d2)
print(ar_zero)
print()
print(ar_zero1)
print()
# one array
arr_one=np.ones(4)
arr_one1=np.ones((3,4))
print(arr_one)      #one d array
print()
print(arr_one1)     #it is use for the 2 d array

# empty array
arra_one=np.empty(4)
arra_one1=np.empty((3,4))
print(arra_one)      #one d array
print()
print(arra_one1)     #it is use for the 2 d array

# range array
array_one=np.empty(4)
print(array_one)      #one d array
print()

#digonal 1's array
ar_dia=np.eye(3)        #it is use for the 2 d array
print(ar_dia)
print()
ar_dia1=np.eye(3,5)       #it is use for the 2 d array
print(ar_dia1)
print()
#linspace 
ar_lin=np.linspace(0,20,num=5)
print(ar_lin)


