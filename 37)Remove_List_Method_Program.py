#Remove Specified Item
#The remove() method removes the specified item.

thislist = ["apple","banana","cherry","kapple"]
thislist.remove("banana")
print(thislist)


#############################################################################


#If there are more than one item with the specified value, the remove() method removes the first occurrence:

#Example
#Remove the first occurrence of "banana":

thislist = ["apple", "banana","cherry","banana","watermelon"]
thislist.remove("banana")
print(thislist)

#############################################################################