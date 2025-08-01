"""
What is a Dictionary in Python?

A dictionary is an unordered, mutable, and indexed collection of key-value pairs.

Key features:
-Unordered
- Mutable ( can be changed after creation)
- Key value pairs
- Fast lookup keys

Real- Life Analogy:
Think of a dictionary like a contact list in your phone:
- Name (key):"Rahul"
- Phone number (value):"9221836894"



"""

"""
# DEFINE A DICTIONARY
 """
 
 # Example 1: Empty Dictionary
empty_dict ={};print(empty_dict)  #output: {}

#Example 2: Student details dictionary with string keys
student ={'name':'Amit','age':21,'grade':'A'};print(student)

# Example 3: Country code mapping
country_code ={'India':'IN','United States':'US'}
print(country_code)

#Example 4: Product price list
products ={'Laptop':55000,'Mouse':500};print(products)
print(products.values())
print(products.keys())

#Example 5: Book info
book ={'title':'Atomic Habits','author':'James Clear','pages':320}
print(book)


"""
CREATE A DICTIONARY (DIFFERENT METHODS)
"""
employees = dict(name="John",salary=25000);print(employees)

#Example 2: Creating from list of tuples from DB or CSV
marks = dict([('Maths',90),('Science',95)]);print(marks)

#Example 3: Creating using zip() - useful when key and values are in separate LISTS.
keys =['email','phone'];values =['abc@gmail.com','1233456789']
contact = dict(zip(keys,values));print(contact)

#Example 4: Using dictionary comprehension - quick generation with logic

squares ={x*x   for x in range(1,4)}
print(squares)

#Example 5: Nested dictionaru - useful for hierarchy and grouped data

company ={

    'HR':{'EMPLOYEES':5,'head':'Asha'},
    'IT':{'Employees':10,'head':'Ravi'}
}
print(company)


"""
ACCESSING DICTIONARY ELEMENTS

"""

# Example 1: Access using key directly
student ={'name':'Amit','age':21};print(student['name'])
# order : Amit 

# Example 2: Using get() method
print(student.get('age')) # Safes way won't raise error
print(student.get('grade'))  #None: Since not present

#Example 3: Loop through Dictionary
for key in student:
    print(key,'->',student[key])


# Example 4: Access keys and values using keys(),values(),items()
print(student.keys())
print(student.values())
print(student.items())

#Example 5: Check if key exists
if 'name' in student:
    print("Name is exists")
else:
    print("Name does not exists")

"""
DICTIONARY 
METHODS

"""

# Example 1: update() - to add or modify key-value pair
profile = {'name':'Shalini'}
profile.update({'email':'shalini@gmail.com'})
print(profile)

#Example 2: pop()- removes a specific key and returns it values
removed_item = profile.pop('email')  #Removes 'email' key
print("Removed",removed_item)

print(profile)


# Example 3: Items() - returns all key values pair as tuple

for key,value in profile.items():
    print(key,value)
    
# Example 4: setdefault()- adds keys with default value if key not present
profile.setdefault('location','India')
print(profile)

#Example 5: clear()
profile.clear();print(profile)


"""
ADDITIONAL USEFUL OPERATIONS

"""

#1. Example : Delete dictonary or a specific key
user ={'name':'Jay','age':22}
del user['age']  #deletes age key


#2. Example : Copy Dictionary ( shallow copy)
original = {'a':1,'b':2}
copied = original.copy()
print(copied)


#3. Example : Merge two dictionaries 
d1 ={'x':10};d2={'y':20}
merged = d1| d2
print(merged)

#4. Length of dictionary
print(f"Number of keys",len(merged))



"""
DICTIONARY OPERATIONS:
# ADD
# UPDATE
# DELETE
# TRAVERSE

"""

# Let's define a dictionary of an online order
order ={
    'order_id':'ord123',
    'customer':'Amit Sharma',
    'items':['Laptop','Mouse'],
    'status':'Processing'
}

#add a new key value pair
order['shipping'] = 'Free'
print(f"After adding shipping info {order}")

# Update the value of an existing key

order['status'] ='Shipped'

# Delete a key-value pair using del
del order['shipping']
print("After removing shipping :",order)

print(order)
# Use pop() to remove and return a key's value
removed_item = order.pop("total_amount")
print("Removed Amount",removed_item)
print("Order after pop",order)


#Loop through keys and values
print("Order details:")
for key,value in order.items():
    print(f"{key} : {value}")
    
    
# Check if a key exists
if 'items' in order:
    print("Items present in order")
    
# Get list of all keys, values and items
print("Keys :", list(order.keys()))
print("Values :",list(order.values()))
print("Key -Value Pairs",order.items())


