marks = {                   #Dictionary stores values in key-value pairs 
    "Rohan": 100,
    "Sushi": 200,
    "NIkita": 400,
    "Kajal":500,
    "Supriya":300
    }

print(marks, type(marks))

print(marks["Kajal"])

print(marks.items())                     #we get value in tuples form by using items

print(marks.keys())                      #we get the marks keys

print(marks.values())                    #we get the values only

marks.update({"Kajal":99})               #update the value of key in dictionary
print(marks)                   

print(marks.get("NIKita"))               #print none

print(marks["NIkita"])                  #print error


 










