ourList = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0
for i in ourList:
    count += i
sumOfList = sum(ourList)
# We can do this by either the sum function that takes the list as the argument and also we can do this by the count that we created using the for loop over our list
avg = sumOfList / len(ourList)
print("Sum = {}".format(count))
print("Average = {}".format(avg))
