ourList = [10, 20, 4, 45, 79, 99]
evenList = []
oddList = []
size = len(ourList)
for i in range(0, size):
    if(ourList[i] % 2 == 0):
        evenList.append(ourList[i])
    else:
        oddList.append(ourList[i])
print(evenList)
print(oddList)
