from functools import reduce

n = int(input())

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# B.extend(A)
# B_string = [str(x) for x in B]
# C = reduce(lambda x,y: x+" "+y,B_string)

A = input().split()
B = input().split()
B.extend(A)
C = reduce(lambda x,y: x+" "+y,B)

print(C)