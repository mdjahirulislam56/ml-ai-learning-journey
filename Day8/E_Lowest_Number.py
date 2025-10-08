n = int(input())

a = input()
temp = a.split()
lst = []
for i in temp:
    lst.append(int(i))

lowest = min(lst)
index = lst.index(lowest)+1
      
print(lowest,index)