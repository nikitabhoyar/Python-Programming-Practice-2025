
thislist = ["apple","mangoes","grapes","avacado","strawberry","cherry"]
print(thislist[2:5])

names = ["Nikita","Nikhil","Prachi","Aditya","Varsha mommy","Papa","Shanshak"]
print(names[1:3])

flowers = ["lily","jasmine","rose","sunflower"]
print(flowers[2:4])


# By leaving out the start value, the range will start at the first item:

thislist = ["apple","banana","cherry","orange","kiwi","kiwi","melon","mangoes"]
print(thislist[:4])


#By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple","banana","cherry","mangoes","kiwi","melon","orange"]
print(thislist[2:])

#Range of Negavtive index 

#Specify negative indexes if you want to start the search from the end of the list:

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple","banana","cherry","orange","kiwi","avacado","grapes"]
print(thislist[-4:-1])

#CHECK IF ITEM IS EXIST OR NOT 

thislist = ["apple","banana","orange","kiwi","avacado","grapes"]
if "apple" in thislist:
    print("yes, Apple is present")

