car_list = [5,4,2,1,3]
def overtake():
    overtaken = 0
    for i in range(len(car_list)):
        for j in range(i,len(car_list)):
            if (car_list[i] > car_list[j]):
                
                overtaken += 1
    return overtaken

print("Total number of overtake is : ", overtake())