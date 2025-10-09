s = input().lower()
x = {}

for char in s:
    x[char]=x.get(char,0) + 1
    
sorted_x = {key : x[key] for key in sorted(x)}
    
for key,value in sorted_x.items():
    print(f"{key} : {value}")