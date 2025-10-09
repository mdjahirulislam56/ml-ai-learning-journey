n,m = input().split()
array = input().split()
A = input().split()
B = input().split()

n = int(n); m = int(m)
array = [ int(i) for i in array ]
A = set([ int(i) for i in A ])
B = set([ int(i) for i in B ])
hapiness = 0


for i in range(n):
    if len(A)==m and len(B)==m:
        if array[i] in A:
            hapiness+=1
        if array[i] in B:
            hapiness-=1

print(hapiness)