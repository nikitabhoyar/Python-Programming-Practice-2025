# Access Tuple Items.

# You can access tuple items by referring to the index number, inside square brackets:

# Example

# Print the second item in the tuple.

thistuple = ("apple","banana","cherry")
print(thistuple[1])

#######################################################################################

# Negative indexing

# Negative indexing start from the end.

# -1 refer to the last item and -2 refer to the second last item.

# Example

# print the last item of the tuple.

thistuple = ("apple","banana","cherry")
print(thistuple[-1])

#############################################################################################

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# Example

# Return the third,fourth and Fifth.

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])

#############################################################################################


# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item: 

# Example

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple","banana","cherry","watermelon","orange","kiwi","melon","orange")
print(thistuple[:4])

##############################################################################################

# By leaving out the end value, the range will go on to the end of the tuple:

# Example 

# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana" ,"cherry","kiwi","watermelon","orange","chiku")
print(thistuple[2:])

############################################################################################

# Range of Negative Indexes.

# Specify negative indexes if you want to start the search from the end of the tuple:

# Example

# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[-4:-1])

##############################################################################################

# Check if Item Exists

# To determine if a specified item is present in a tuple use the in keyword:

# Example

# Check if "apple" is present in the tuple:

thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("Yes, apple is present in tuple")


###############################################################################################















