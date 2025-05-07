import numpy as np

var=np.array([1,2,3,4])

co=var.copy()

var[1]=40

print("var : ",var)
print("copy : ",co)


x=np.array([9,8,7,6,5])

vi=x.view()

x[2]=30

print("x : ",x)
print("view : ",vi)

