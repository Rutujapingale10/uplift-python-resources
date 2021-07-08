car_list = input("Enter the list : ")
car_list =  car_list.split()
def overtake():
    overtaken = 0
    overtaken = [(overtaken+1) for i in range(len(car_list)) for j in range(i,len(car_list)) if (car_list[i]>car_list[j])]
    return len(overtaken)

print("Total nnumber of overtake is : ", overtake())
