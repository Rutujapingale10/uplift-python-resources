
def racecar(lst):
    n = len(lst)
    average = 0
    for i in range(n):
        for j in range(0,len(lst)-1):



# traverse the list from 0 to len(lst)-1
# Swap if the element found is greater
# than the next element

         if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
  
        average += 1

    return average
 
# Driver Code
lst = [4,3,1,2,5]

print(f"total count is {racecar(lst)}")