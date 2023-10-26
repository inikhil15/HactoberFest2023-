import numpy as np
def show(matrix):
    for i in range(0,len(matrix)):
        print(matrix[i])
        
m1=[]
m2=[]
res=[]
print("Enter no. of rows : ")
m=int(input())
n=m
print("Input for Matrix:1")
for i in range (0,m):
    row=[]
    for j in range(0,n):
        print("Enter element no. (",i,",",j,"):")
        row.append(int(input()))
    m1.append(row)
print("Input for Matrix:2")
for i in range (0,n):
    row=[]
    for j in range(0,m):
        print("Enter element no. (",i,",",j,"):")
        row.append(int(input()))
    m2.append(row)

res=np.dot(m1,m2);
show(m1)
print("x")
show(m2)
print("=")
show(res)
