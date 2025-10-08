a = input()

x, min_v, max_v = a.split()

x = float(x)
min_v = float(min_v)    
max_v = float(max_v)


if max_v > min_v:
    norm = (x - min_v) / (max_v - min_v)
    
    print( f"{norm:.2f}")

