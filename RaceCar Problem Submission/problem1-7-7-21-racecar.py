"""
There are n cars. And their locations are represented by their List Indexes.
e.g. [4,1,2,3]
So,
1. The Index is the Location. (4 is in the last. 3 is in the first as per the distance is concerned)
2. The value of the elements is the speed. (So, 4 is the 0th Index Car's speed)

If a and b are two cars in the list. And if a is on the left and b is on the right. Which in this case means that a is behind b

The required solution is:
If location(a)<location(b), but speed(a)>speed(b), a will at some point overtake b

So, let's say 4 3 1 2 is the list.
Now, 3 is ahead of 4 but it is less than 4, so at somepoint 4 will overtake 3.
The same goes for 1 and 2 both. They are both ahead of 4 but their speed/value is less than 4. So, at some point 4 will overtake 1 & 2
So, in total 4 will overtake 3 cars

3 will overtake 2 cars.

Both 1 and 2 will overtake no cars.

So, in total there are 3+2 = 5 overtakes.append

Consider the above condition and write a Python Program to calcaulate the total overtake for the below given list.
"""
Arr = list(map(int, input().split()))
overtakeCount = 0
for i in range(len(Arr)):
    for j in range(i+1, len(Arr)):
        if(i < j and Arr[i] > Arr[j]):
            overtakeCount += 1
print(overtakeCount)
