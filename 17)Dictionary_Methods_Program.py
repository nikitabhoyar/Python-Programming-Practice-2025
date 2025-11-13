#Dictionary clear method in Python
my_dict = {'name':'Nikita','age':26}
my_dict.clear()
print(my_dict)

#dict_copy() method
my_dict = {'name':'Nikita', 'age':25}
new_dict = my_dict.copy()
print(new_dict)

#🧩dict.fromkeys() method
#Creates a new dictionary from the given sequence of keys with a specified value.
keys = ['name','age','cityt']
new_dict = dict.fromkeys(keys,'Unknown')
print(new_dict)

#🧩 4. dict.get()
#Returns the value for a specified key; returns None if the key doesn’t exist.
my_dict = {'name': 'Nikita', 'age': 26}
print(my_dict.get('name'))
print(my_dict.get('city','Not found'))

#🧩 5. dict.items()
#Returns a list of tuples containing key-value pairs.
my_dict = {'name':'Shruti', 'age':26}
print(my_dict.items())

#🧩 6. dict.keys()
#Returns all the keys of the dictionary.
my_dict = {'name':'Neha', 'age':26}
print(my_dict.keys())


#🧩 7. dict.values()
#Returns all the values of the dictionary.
my_dict = {'name':'Nikita', 'Age': 26}
print(my_dict.values())

#🧩 8. dict.pop()
#Removes the specified key and returns its value.
my_dict = {'name':'Nikita','age':26,'Class': 12}
age = my_dict.pop('age')
print(my_dict)

#🧩 9. dict.popitem()
#Removes and returns the last inserted key-value pair (LIFO order).
my_dict = {'name':'Nikita', 'age':27 , 'City': 'pune'}
popitem = my_dict.popitem()
print(popitem)

#🧩10. dict.setdefault()
#Returns the value of a key; if not found, inserts the key with a specified default value.
my_dict = {'name': 'Nikita'}
value = my_dict.setdefault('age', 26)
print(value)     # Output: 26
print(my_dict)   # Output: {'name': 'Nikita', 'age': 26}

my_dict = {'name': 'Nikita'}
value = my_dict.setdefault('age', 26)
print(value)     # Output: 26
print(my_dict)   # Output: {'name': 'Nikita', 'age': 26}

my_dict = {'name': 'Nikita'}
value = my_dict.setdefault('age', 26)
print(value)     # Output: 26
print(my_dict)   # Output: {'name': 'Nikita', 'age': 26}

my_dict = {'name': 'Nikita'}
value = my_dict.setdefault('age', 26)
print(value)     # Output: 26
print(my_dict)   # Output: {'name': 'Nikita', 'age': 26}


#🧩 11. dict.update()
# #Updates the dictionary with key-value pairs from another dictionary or an iterable.
my_dict = {'name': 'Nikita', 'age': 26}
my_dict.update({'city': 'Nagpur'})
print(my_dict)  # Output: {'name': 'Nikita', 'age': 26, 'city': 'Nagpur'}








