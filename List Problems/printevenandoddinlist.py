ourList = []
for i in range(0, 7):
    ourList.append(int(input()))
print(ourList)
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
print(f"There were {len(evenList)} Even Numbers in the first list and {len(oddList)} Odd Numbers in the first list")
