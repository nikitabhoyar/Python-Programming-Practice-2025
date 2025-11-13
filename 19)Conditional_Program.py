
#IF elseif else ladder

age = int(input("Enter your age:"))

if(age>=18):
    print("You are eligible for vote")
elif(age<0):
    print("You are entering an invalid negative age")
elif(age==0):
    print("Youare entering 0 which is not valid age")
else:
    print("You are not eligible for vote")

print("End of the program")

