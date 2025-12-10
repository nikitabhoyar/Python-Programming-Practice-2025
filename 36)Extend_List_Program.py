
#To append elements from another list to the current list, use the extend() method.

#Example
#Add the elements of tropical to thislist:

thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","grapes"]
thislist.extend(tropical)
print(thislist)

#####################################################################################

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

thislist = ["apple","banana","cherry","orange","watermelon"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
