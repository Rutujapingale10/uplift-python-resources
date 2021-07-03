"""
eydb -> bdey
dbcb -> bbcd
"""
string = "sagnik"
"""
So, now the length of the string is 6
We need to convert this string to a list
So, we are running a loop in that string, and 
in that loop we are appending that partiucalr indexed element to that list
So, here ourlist is mylist.
So, we are appedning "s", then "a" and so on and so forth 
and now, we are soprting the list because that's what the question ask
and also, we need to conevery it to a string
"""
mylist = []
for i in range(len(string)):
    mylist.append(string[i])
mylist.sort()
"""
Now, this is how we convery a list to a string
We basically adds the list elements to the string
By uising the += method 
We can also do it by writign  str1 = str1+list[i]
"""
res_str = ""
for j in mylist:
    res_str += j
print(res_str)
