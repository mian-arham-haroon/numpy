import numpy as np

#array
x=[1,2,3,4,5]

y=np.array(x)

print(y)
print(type(y))
ar2=np.array([[1,2,3,4,5],[1,2,3,4,5]]) #it is 2d array
print(ar2)
print(ar2.ndim)

ar3=np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]]) #it is 3d array
print(ar3)
print(ar3.ndim)

arn=np.array([1,2,3,4,5],ndmin=10) #it is multi d array
print(arn)
print(arn.ndim)

# print(y.ndim)  #that is use for chack the dimension
# l=[]
# for i in range(1,5):
#     int_1=int(input("enter:"))
#     l.append(int_1)

# print(np.array(l))  



