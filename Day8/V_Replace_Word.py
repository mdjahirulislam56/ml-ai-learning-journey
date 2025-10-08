s = input()
s_upper = s.upper()

if "EGYPT" in s_upper:
    s_replaced = s.replace("EGYPT"," ")
    print(s_replaced)
else:
    print(s_upper)