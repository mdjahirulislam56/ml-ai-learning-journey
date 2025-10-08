n = input()

pixels = n.split()

if (len(pixels)>=1) and (len(pixels)<=100):
    sum = 0
    count = 0
    for i in pixels:
        pixel_value = int(i)
        if (pixel_value>=0) and (pixel_value<=255):
            sum += pixel_value
            count += 1 
    avg_brightness = sum/count
    
    if avg_brightness<85:
        print("Dark Image")
    if avg_brightness>=85 and avg_brightness<=170:
        print("Normal Image")
    if avg_brightness>170 and avg_brightness<=255:
        print("Bright Image")