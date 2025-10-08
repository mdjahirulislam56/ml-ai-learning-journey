a = input()

brightness , threshold = a.split()

brightness = float(brightness)
threshold = float(threshold)


if brightness >= threshold:
    print("ON",end="")
else:
    print("OFF",end="")