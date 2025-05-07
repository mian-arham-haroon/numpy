import numpy as np

var=np.array([1,2,3,4,5,6,7,8])
print(var)
print()
for i in var:
    print(i)
var1=np.array([[1,2,3,4],[5,6,7,8]])

for j in var1:
    print(j)
for k in var1:
    for g in k:
        print(g)    

var2=np.array([[[1,2,3,4],[5,6,7,8]]])

for j in var2:
    print(j)
for k in var2:
    for g in k:
        for n in g :
            print(n) 



var2=np.array([[[1,2,3,4],[5,6,7,8]]])

for j in np.ndenumerate(var2):
    print(j)

# for j,d in np.nditer(var2,flags=['buffered'],op_dtypes=['S']):
#     print(j,d)




