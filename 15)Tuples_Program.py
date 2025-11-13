a = (1,2,3,4,6,8,9,"Nikita", False , True , 123)
print(a)

#count() method 
numbers = (1, 4,3 , 5 , 7 ,6, 8,9)
count_2 = numbers.count(3)
print("Numbers of times 3 appears", count_2)

#index() method 
#find index of first occurence
letters = ("a", "b","d","r","y","w")
letters_b = letters.index("b")
print(letters_b)

#len() function 
tup = ("apple","banana","sweeter", "orange")
print("Length of tuple is",len(tup))


#max and min method
marks = (12,45,78,90,34)
print("Maximum marks:", max(marks))
print("Minimum marks:",min(marks))


#sum() tuple function
numbers = (12, 56 ,34 ,78 ,90)
print("Sum of numbers is :", sum(numbers))


#tuple() convert list to tuple
fruits = ["Apple" , "Banana" , "Orange", "Chicku", "Mongo"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)

#Membership in / not 
color = ("Red","Pink","Yellow","White")
print('Red'in color)              #true
print('White' not in color)       #true

#Concenation method()
t1 = (1,2,3)
t2 = (4,5,6)
t3 = (t1 + t2)
print("Concatenations of tuple",t3)

#Repetition method
msg = ('Hello',)
print(msg * 3)

#Slicing method()
nums = (10 , 20 , 30 ,56 ,89)
print("slice",nums[1:4])

