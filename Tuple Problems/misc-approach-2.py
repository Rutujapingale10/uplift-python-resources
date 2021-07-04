result_list = []
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
list4 = [7, 8, 9]
tuple1 = (11, 12)
tuple2 = (13, 14)
tuple3 = (15, 16)
tuple4 = (17, 18, 19)
lis = [list1, list2, list3, list4]
tup = [list((tuple1)), list((tuple2)), list((tuple3)), list((tuple4))]
opList = []


def otpList(lis, tup):
    usIp = int(input("Enter 1 for tuple and 2 for list : "))
    if(usIp == 1):
        for i in range(8):
            if (i % 2 == 0):
                opList.append(tup[int(i / 2)])
            else:
                opList.append(lis[int(i / 2)])
    elif(usIp == 2):
        for i in range(8):
            if (i % 2 == 0):
                opList.append(lis[int(i/2)])
            else:
                opList.append(tup[int(i/2)])
    else:
        print("WRONG INPUT SORRY !!!")
        exit()
    return opList


print(otpList(lis, tup))
