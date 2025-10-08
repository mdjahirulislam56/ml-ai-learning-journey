n = int(input())

count_yes = 0
count_no = 0
if int(n)>=1:
    for i in range(n):
        vote = input()
        if "YES" in vote:
            count_yes+=1
        if "NO" in vote:
            count_no+=1

if count_no <= count_yes:
    print("ACCEPT")
else:
    print("REJECT")