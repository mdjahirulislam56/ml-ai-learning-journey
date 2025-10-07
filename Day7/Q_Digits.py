n = int(input())
num = []

for i in range(n):
    numbers = input()
    num.append(numbers)

for s in num:
    for i in s[::-1]:
        print(i,end=' ')
    print()

