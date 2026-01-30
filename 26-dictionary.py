"""DICTIONARY"""
# A dictionary stores data as key-value pairs. Each key is unique and is ued to get its value. Dictionaries are useful when you want to store and find data using a name(key) instead of position number like in a list or tuple. They are unordered, mutable(changeable) and do not allow duplicate key.

# Key should be of data type which is immutable and value could be both mutable or immutable.


"""1. Creating a Dictionary"""
# A dictionary is created using curly brackets {}, where each key is linked to a value using a colon (:). We can also create a dictionary using the dict() function.

# For a empty dictonary we use {}.

d1 = {1: 'Aman Singh',
      2: 'Shashi Singh',
      3: 'Alok Singh'}
print(d1)

d2 = dict(a='Aman Singh', b='Shashi Singh', c='Alok Singh')
print(d2)


"""2. Accessing Dictonary Items"""
# A value in a dictonary is accessed by using its keys. This can be done either with square brackets [] or with the get() method. Both return the value linked to the given key.

d = {"name":"Aman Singh","Age":25, (1,2):[1,2,3]}
print(d["name"]) # Using Key
print(d.get((1,2))) # Using get()


"""3. Removing Items"""
# Dictonary items can be removed using built-in deletion methods that work on keys:
# 1. del : removes an item using its key
# 2. pop() : removes the item with the given key and returns its value
# 3. clear() : removes all items from the dictonary
# 4. popitem() : removes and returns the last inserted key-value pair

d = {1:'Aman Singh', 2:'Shashi Singh', 3:"Alok Singh", "age":23}
print(d)

del d['age'] # usingh del
print(d)

val = d.pop(1) # using pop()
print(val)

key , value = d.popitem() # using popitem()
print(f"Key : {key}, Value: {value}")

d.clear() # using clear()
print(d)


"""4. Reassigning a Value"""
# You can change (reassign) a value in a dictonary by using its key.

student = {
    "name": "Aman",
    "age": 20
}
print(student)

student['age'] = 22
print(student)


"""5. Adding a New Key–Value Pair"""
# You can add a new key and value to a dictonary by using the assignment operator (=) with a new key.

student = {
    "name": "Alice",
    "age": 20
}
print(student)

student["Surname"] = "Yadav"
print(student)


"""6. Nested Dictonary"""
# A nested dictonary is a dictonary that contains another dictonary as one of its value.

student = {
    "name" : "Aman",
    "details" : {
        "age" : 15,
        "grade" : "A+",
        "city" : "New York"
    }
}

print(student)
print(student["details"]["city"]) # Accessing in nested dictonary


"""7. Dictonary methods"""
# 1. myDict.keys() : returns all keys
# 2. myDict.values() : returns all values
# 3. myDict.items() : returns all key-value pair as tuples
# 4. myDict.get("key") : returns the key according to value
# 5. myDict.update(newDict) : inserts the specified item to the dictonary

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"id": 112})
print(student)

print(len(student))
