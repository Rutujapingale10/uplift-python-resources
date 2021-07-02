# Find the Maximum and Minimum K elements in a Tuple
# """
# It is immutable
# So, we can't change the elemtns of the tuple
# So, we can't modify direct like the list problem
# But, there is a big chance that we can cast it to a List and then solve the problem with
# but it is alwasy better if we can solve directly staying within a Tuple

# Input: (3,7,1,18,9) k = 2
# Output: (1,3,9,18)
# """
k = int(input("Enter the K Value: "))
total_entry = int(input("How many numbers you want in your tuple: "))
ourList = []
for i in range(total_entry):
    ourList.append(int(input(f"Enter the {i+1}th Entry: ")))
ourList.sort()
newList = ourList[:k]+ourList[-k:]
# for i in range(k):
#     newList.append(ourList[i])
#     newList.append(ourList[-1-i])
newList.sort()
ourTuple = tuple(newList)
print(ourTuple)
