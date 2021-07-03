"""
list - random list
now we need to do the average of the second highest and the second lowest element of that list
so to do that, first we need to sort the lisr
and after soprting, so we have the 2nd elemt or the element with index 1 as the 2nd lowest elentn
and the 2nd last element or the elemtn with index [len(list)-2] asd the 2nd highest element
now we just need to do the average of them
"""
ourList = [13, 1, 2, 7, 4, 6, 89, 23, 8]
ourList.sort()
result = float((ourList[1]+ourList[-2])/2)
print(f"The output average will be {result}")
