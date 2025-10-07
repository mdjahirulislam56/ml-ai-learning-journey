n = int(input())
numbers = input()
num = numbers.split(' ')

even = 0
odd = 0
positive = 0
negative = 0

for i in range(n):
    
    if int(num[i])%2==0:
        even += 1
    else: 
        odd += 1
    
    if int(num[i])>0 :
        positive+=1
    elif int(num[i])<0:
        negative+=1

print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")