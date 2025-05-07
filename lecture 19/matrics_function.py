import numpy as np

var=np.matrix([[1,2],[4,5]])

# print(np.transpose(var))
# print(var.T)
# print(np.swapaxes(var,0) )

# print(np.linalg.inv(var))
# print(np.linalg.matrix_power(var,2)) 
print(np.linalg.det(var))


