# The Elif Keyword:

# The elif keyword is Python's way of saying
# "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and 
# execute a block of code as soon as one of the conditions evaluates to True.

a = 33
b = 33
if b > a :
    print("b is greater than a")
elif a == b :
    print("a and b are equal")


# Multiple Elif Statements

# You can have as many elif statements as you need.
# Python will check each condition in order and 
# execute the first one that is true.

score = 75 

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >=60:
    print("Grade D")
elif score >= 50:
    print("Grade E")


# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. 
# This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

#Example
#Day of the week Checker

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thrusday")
elif day == 5:
    print("Friday")
elif day == 6: 
    print("Saturday")
elif day == 7:
    print("Sunday")

    