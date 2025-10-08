n = int(input())

a = input()
temp = a.split()
lst = []
for i in temp:
    lst.append(int(i))

max = max(lst)
min = min(lst)

max_ind = lst.index(max)
min_ind = lst.index(min)

lst[max_ind]=min
lst[min_ind]=max

for i in lst:
    print(i,end=" ")