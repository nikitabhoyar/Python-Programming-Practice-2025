#Remove specified index.

#The pop() method removes the specified index 

#Example 

#Remove the second item.

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

#########################################################################################

#if we do not specify the index , the pop() method removes the last item.

#Example.

#Removes the last item.

names = ["nikita","chaku","prachi"]
names.pop()
print(names)

#####################################################################################33

#The del keyword also removes the specified index.

#Example

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#################################################################################

#The del keyword can also delete the list completely.

thislist = ["apple","banana","cherry"]
del thislist 

###############################################################################
