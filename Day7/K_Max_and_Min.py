ABC = input()
A,B,C = ABC.split(' ')

A = int(A)
B = int(B)
C = int(C)

min = A
max = A 

if (max<B):
    max = B
if (max<C):
    max = C
if (min>B):
    min = B
if (min>C):
    min = C
    
print(min,max)
