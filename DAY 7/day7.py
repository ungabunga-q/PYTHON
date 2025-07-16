""" DAY - 7
TUPLE
"""

"""
A tuple is a built-in data structure in Python that allows you
to store multiple items in a single variable.

Tuples are:
#1. Ordered ( items have a fixed position)
#2. Immutable ( cannot be changed after creation)
#3. Can contain duplicate values
#4. Represented wing parentheses ()

"""

#Defining a tuple
#1. Defining tuple with integers
numbers =(1,2,3,4,5);print(numbers);print(type(numbers))

#2. Tuples with mixed datatype
info =("Alice",25,5.6,True);print(info);print(type(info))

#3. Tuple with a single element ( add a comma)
single_element =(10,);print(single_element);print(type(single_element))

#4. Empty Tuple
empty = ();print(empty);print(type(empty))

""" 
Creating a Tuple

"""

#1. Example 1 : Tuple of fruits
fruits = ("apple","banana","cherry");print(fruits)

#2. Tuple using tuple constructor from a list
a =['red','green','blue'];colors =tuple(a);print(colors)

#3. Tuple with mixed datatypes
nested = ((1,2),(3,4));print(nested)

#4. Tuple with mixed datatype
person = ("John",30,'Engineer',True);print(person)

#5. Tuple from a string ( each character becomes an element)
chars =tuple("Hello");print(chars)


""" 
Accessing Elements of the Tuple

"""

#1. Example : Indexing
t = ('a','b','c','d');t[:3]

#2. Negative Indexing 
print(t[-1]) #output : d

#3. Slicing
print(t[1:3]) #output: ('b','c')

#4. Interating through a tuple

for item in t:
    print(item)
    
#5. Length of the Tuple
print(len(t)) #output : 4


""" 
What is immutability?

Tuples are immutable, meaning once created, their elements
cannot be changed,added or removed.

"""

#Example of immutability
my_tuple = (10,20,30) ;#my_tuple[1]=6565

#However you can replace the whole tuple
my_tuple =(100,200);print(my_tuple)

"""
List vs Tuple

Lists are mutable, meaning their elements can be changed,added or removed after creation.
Tuples are immutable, meaning their elements cannot be changed,added or removed after creation.


----------------------------------------------------------------------------------
Feature          | List                | Tuple
----------------------------------------------------------------------------------
Mutability      | Mutable               | Immutable
Syntax          | [] (square brackets)  | () (parentheses)
Performance     | Slower (due to mutability) | Faster (due to immutability)
Methods Many    |built-in methods       | Fewer methods available (count, index)
Use Cases       | Frequent updates      | Fixed collections or read-only data
----------------------------------------------------------------------------------
Order          | Ordered             | Ordered
----------------------------------------------------------------------------------
Duplicates      | Can contain duplicates | Can contain duplicates
----------------------------------------------------------------------------------
Hashable        | Not hashable       | Hashable (can be used as dictionary keys)
----------------------------------------------------------------------------------
Memory Usage   | More memory usage  | Less memory usage


"""
    
#Example of list vs tuple
my_list = [1,2,3,4];print(type(my_list)) #output: <class 'list'>
my_tuple = (1,2,3,4);print(type(my_tuple)) #output: <class 'tuple'>

#Tuple Operations:

#1. Example 1 : Concatenation ( Combining two tuples into one)
t1 = (1,2);t2 = (3,4);print(t1 + t2)  #output: (1, 2, 3, 4)

#2. Repetition (repeating elements in a tuple)
print(t1*4)  #output: (1, 2, 1, 2, 1, 2, 1, 2)

#3. Membership Test (Checks if the element 2 exists in the tuple)
print(2 in t1)  #output: True

#4. Count of an element
t3=(1,2,3,3,2);print(t3.count(2))  #output: 2

#5. Index of an element
print(t3.index(3))  #output: 2 (returns the first occurrence index of the element)  


#6. Converting a list to a tuple
my_list=[10,20,30] ;converted_t = tuple(my_list) 
print(converted_t)  #output: (10, 20, 30)

#7. Tuple unpacking
student =('John', 20, 'A');name,age,course =(student);
print(name)  #output: John
print(age)   #output: 20    
print(course)  #output: A
print(f"Name: {name}, Age: {age}, Course: {course}")  #output: Name: John, Age: 20, Course: A


#8. Nested Tuples
data =(('Alice','HR'),('Bob','IT'),('Charlie','Sales'))
print(data)  #output: (('Alice', 'HR'), ('Bob', 'IT'), ('Charlie', 'Sales'))
print(data[1][0])  #output: Bob (accessing nested tuple element)


#9. Iterating over a tuple
colors =("Red",'blue','green')
for color in colors:
    print(color)
    

#10. Tuple with mixed data and type checking (Prints type of each element in the tuple)
employee = ('EOO1',"Shalini",28,True)
for item in employee:
    print(f"{item}------> {type(item)}")
    
    
# Real world data analysis example using Tuplr

""" 
Problem:
You are analysing a product sales dataset where each record is a tuple:
(Product_Name, Category, Price, Quantity Sold)

Objectives:
Calculate total sales and find out the most sold product.
"""

#List of sales records tuple.
sales_data =[
    ('Laptop','Electronics',50000,10),
    ('Mouse','Electronics',500,50),
    ('Shirt','Clothing',800,30),
    ('Book','Stationary',300,40),
    ('Pen','Stationary',20,200),
]

total_sales =0;max_sold=0;top_product =""


""" total sales """
for item in sales_data:
    name,category,price,qty = item
    sale = price*qty
    total_sales+=sale
    
# remaining code check 

    
    

    

