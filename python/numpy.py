import numpy as np
m=[]
n=int(input("enter the number of values:"))
print("enter the values")
for i in range(n):
    a=[]
    a.append(int(input()))
    m.append(a)

mean1=np.mean(m)
print("mean of value: ",mean1)

median1=np.median(m)
print("median of values:",median1)

min1=np.min(m)
print("minimum values:",min1)

max1=np.max(m)
print("maximum values:",max1)

sum=np.sum(m)
print("sum of values:",sum)

sq=np.sqrt(m)
print("square root values:",sq)