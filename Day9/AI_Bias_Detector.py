a = input()

pred_lst = a.split()

count_A = 0
count_B = 0

if (len(pred_lst)>=1) and (len(pred_lst)<=100):
    for i in pred_lst:
        if "A" in i:
            count_A +=1
        if "B" in i:
            count_B +=1
    
    percent_A = (count_A / (count_A + count_B))*100
    percent_B = (count_B / (count_A + count_B))*100
    
    if (percent_A > 70) or (percent_B > 70):
        print("Biased Model")
    elif (percent_A>=0) or (percent_B>=0):
        print("Fair Model")
    

