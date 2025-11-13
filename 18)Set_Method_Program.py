set = {1,2,4,5,6,5,6,7,7,8}
print(set)                  #Ins set the values are not repeat means no pepetition.

set.add(90)                 
print(set)

#1. add()
#Adds a single element to the set.

fruits = {'apple','bananna','orange','chiku','custurd_apple'}
fruits.add('Mango')
print(fruits)

#2. update()
#Adds multiple elements (from list, tuple, set, etc.) to the set.

Name = {"Aman", "Nikita", "Shruti", "Neha" , "Riya" , "Sujata"}
Name.update(["Suyash"])
print(Name)

#3. remove()
#Removes the specified element.
#Raises an error if the element doesn’t exist.

fruits = {"apple","Banana","Orange","Chiku"}
fruits.remove("Banana")
print(fruits)


#4. discard()
#Removes the specified element if it exists (no error if not found).
colors = {"Red","Pink","Purple","Orange","White"}
colors.discard("Orange")
print(colors)

#🔹 5. pop()
#Removes and returns a random element from the set.
fruits = {"Apple","Chiku","Custard_Apple","Berry","Banana"}
item = fruits.pop()
print(item)
print(fruits)

#🔹 6. clear()
#Removes all elements from the set
Names = {"Aman","Sujata","Pagal","Mad","Stupid","Mental"}
Names.clear()
print(Names)

#🔹 7. copy()
#Returns a shallow copy of the set.
fruits = {"Mango","Chiku"}
new_fruits = fruits.copy()
print(new_fruits)

#8. union()
#Returns a new set with all unique elements from both sets.
fruits = {"Apple","Mango","Justein"}
Names = {"Aman","Nikita"}
print(fruits.union(Names))

#🔹 9. intersection()
#Returns a set containing only common elements.
Names = {"Chiku","Mango"}
Fruits = {"Aman","Gupta"}
print(Names.union(Fruits))

#🔹 10. difference()
#Returns elements present in one set but not in the other.
a = {1 ,2 , 3}
b = {4 , 2 , 4 , 3}
print(a.difference(b))

#🔹 11. symmetric_difference()
#Returns elements that are in either set but not both.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))   # {1, 2, 4, 5}

#🔹 12. issubset()
#Checks if all elements of one set are in another.
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True

#13. issuperset()
#Checks if the set contains all elements of another set.
a = {1,2 ,3}
b = {1 , 2 }
print(a.issuperset(b))

#🔹 14. isdisjoint()
#Checks if two sets have no elements in common.
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  














