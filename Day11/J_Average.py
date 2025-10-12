from functools import reduce

n = int(input())
A = list(map(float,input().split()))

sum = reduce(lambda x,y: x+y , A)
avg = sum/len(A)

print(f"{avg:.7f}")