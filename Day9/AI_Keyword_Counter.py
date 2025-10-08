a = input()

message = a.split()

lst = ["ai", "data", "model", "learn", "train", "neural"]

count = 0
for i in lst:
    if i in message:
        count +=1
if count>=2:    
    print("AI Detected")
else:
    print("Not AI Related")