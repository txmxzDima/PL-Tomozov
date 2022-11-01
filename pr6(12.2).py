import random
A=[]
B=[]
for i in range(10):
   A.append(random.randint(0,100))
for i in range(10):
   B.append(random.randint(0,100))
print(A)
print(B)
temp = 0
for i in range(10):
   temp = A[i]
   A[i]=B[i]
   B[i]=temp
print(A)
print(B)