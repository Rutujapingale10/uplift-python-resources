#Defining the given list
carList = [4, 1, 2, 5]
overtake = 0

for i in range(len(carList)):
    for j in range(0, len(carList) - 1):
        if carList[j] > carList[j + 1]:
            carList[j], carList[j + 1] = carList[j + 1], carList[j]
            overtake += 1
print(f"Number of overtakes are : {overtake}")