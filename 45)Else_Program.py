# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33

if b > a:
    print("b is greater than a ")
elif a == b:
    print("A is equal to b")
else:
    print("a is greater than b")

#####################################################################################################


# Else Without Elif

# You can also have an else without the elif:

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


######################################################################################################

# Complete If-Elif-Else Chain   
# You can combine if, elif, and else to create a comprehensive decision-making structure.

# Example

temperature = 22

if temperature > 30:
    print("It's too hot outside")
elif temperature > 20:
    print("its warm outside")
elif temperatur > 10:
    print("Its cool outside")
else:
    print("Its cool outside")







