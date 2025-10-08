n = int(input())

target = float(input())

sum = 0
count = 0
for i in range(n):
    loss = float(input())
    sum+=loss
    count+=1
avg = sum/count

if avg <= target:
    print("PASS")
else:
    print("RETRY")