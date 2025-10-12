from functools import reduce 
n = int(input())

lst_num = list(map(int,input().split()))

# max = reduce(lambda x,y: x if x>y else y, lst_num)
# min = reduce(lambda x,y: x if x<y else y, lst_num)
# print(min,max)

min_max = lambda l: (sorted(l)[0], sorted(l)[-1])
min,max = min_max(lst_num)
print(min,max)