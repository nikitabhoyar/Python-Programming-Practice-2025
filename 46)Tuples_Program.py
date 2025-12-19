# Tuples are used to store multiple items in a single variable.

# Tuples is one of the 4 buit in data types in python used to store collection of data . 

# The other three are List,set and dictionary . All with different qualities and usage.

# A tuple is collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Example

thistuple = ("apple","banana","cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

#######################################################################################################################

# Tuple Length

# To determine how many items the tuple has , use the len() function.

# Example

# Prin the number of items in the tuple 

thistuple = ("apple","banana","cherry")
print(len(thistuple))

#######################################################################################################################

# Create Tuple with one item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example

# One item tuple , remember the comma.

thistuple = ("apple",)
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple))

#########################################################################################################################

# Tuple Items - Data Types 

# Tuple items can be of any data type.

# Example.

tuple1 = {"apple","banana","cherry"}
tuple2 = {True,False}
tuple3 = {1,2,3,4,5,6,7,9}
print(tuple1,tuple2,tuple3)

#########################################################################################################################

# Example

# A tuple with string,integers and boolean value.

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# <class 'tuple'>
# Example

# What is the data type of a tuple?

mytuple = ("apple","banana","cherry")
print(type(mytuple))

###########################################################################################################################

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Example
# Using the tuple method to make a tuple.

thistuple = tuple(("apple","banana","cherry","watermelon"))
print(thistuple)




