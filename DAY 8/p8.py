"""
17th JULY 2025
WHAT IS A SET?
1. A set is an unordered collection of unique elements.
2. It removes duplicates automatically.
3. It is mutable, meaning you can add or remove elements after creation.
4. Elements inside a set must be immutable ( eg: numbers, strings, tuples)
5. Sets are defined using:
        - Curly braces: {}
        - set() constructor
6. Sets support mathematical operations like:
    - Union
    - Intersection
    - Difference
    - Symmentric Difference
    


"""

#-----------------------------------------------------------------
# Defining a set
#-----------------------------------------------------------------

#1. Example 1 : Define a set using curly braces
my_set={1,2,3};print(f"Example 1: {my_set}")

#2. Example 2 : Create a set from a lists using set() constructor
numbers = set([1,2,3,4]);print(f"EXAMPLE 2: {numbers}")

#3. Example 3 : Duplicates are removed automatically
sample = {1,2,2,3,4,4,5};print("Example 4 is",sample)

#4. Example 4: Set with multiple datatypes
mix = {10,"apple",3.14};print(f"Example 4 : {mix}")

#5. Example 5: Creating an empty set
empty = set() # creates an empty dictionary, not a set
print(f"Example 5 [empty set] {type(empty)}")


#------------------------------------------------------
# Creating a set Dynamically
#------------------------------------------------------


# Example 1: Create a set from a string ( characters only, Duplicates removed)
chars = set("Aishwarya");print(f"Dynamic Example 1 {chars}")

# Example 2 : Create a set from a list with duplicates
list_set = set(['apple','banana','apple']);print(f"Dynamic Example 2 {list_set}")

# Example 3 : Create a set from tuple
tuple_set = set((1,2,3,2));print("Dynamic Example from {tuple is }:",tuple_set)

# Example 4: Create a set using range()
range_set = set(range(5));print(f"Dynamic Example 4 range :{range_set}")

# Example 5 : Create a set from user input
items =input("Enter items separated by space:").split()
user_items = set(items);print(f"Dynamic Example 5:{user_items}")

""" 
SET OPERATIONS 

"""
a = {1,2,3};b={3,4,5}

# Example 1 : Union - combin

""" 
SET METHODS
"""
fruits ={'apple','cherry','banana'}

# Example 1: add() - Adds new element
fruits.add("orange");print(f"After add {fruits}")

#Example 2: remove() - Removes element, raises error if element not found
fruits.remove('banana')
print(f"After remove :{fruits}")

#Example 3:discard() - Removes element, no error if element not found
fruits.discard("grape");print(f"After remove: {fruits}")

#Example 4: pop()- Removes and returns a random element
removed_items = fruits.pop()
print(f"Removed by pop(): {removed_items}")
print("After pop(),",fruits)

#Example 5: clear()- Removes all elements from the set
fruits.clear();print(fruits) #OUTPUT SET()

""" 
SET OPERATIONS 

Set operators:
1. Python sets support mathematical operations similar to those in set theory.
2. These operations are useful when working with collections of unique items.
3. Sets automatically remove duplicates
4. Main operations include-
    - Union:
    - Intersection:
    - Difference
    - Symmentrical Difference
    - Membership Test

"""

"""
#1. Union (| or .union()):
Combines all elements from both sets. Duplicate values are removed.
"""
set1 = {1,2,3};set2={3,4,5}
print("Union using | :",set1 | set2)

# Using union() method
print("Union using union",set1.union(set2))

""" Intersection (& or .intersection()):
Returns only the elements that are common in both sets

"""
set1={1,2,3,4};set2={3,4,5,6}
intersection_result = set1 & set2

print(f"Intersection using &:",intersection_result)

# Using intersection() methods
print(f"Intersection using intersection(): {set1.intersection(set2)}")

"""
3. DIFFERENCE(- ot .difference())

Returns elements present in the first set only, not the second
"""

set1 ={1,2,3,4};set2={3,4,5}
#using - operator
print(f"Difference [set1 - set 2]; {set1- set2}")

#using difference operator
dif_operator= set1.difference(set2)
print(dif_operator)

""" 
4. Symmentrical Difference( ^ or .symmentrical_difference())
Returns elements that are either set, both not in both

"""

set1 ={1,2,3}
set2 = {3,4,5}

# Find union using ^ operator
symmentric_difference_result = set1 ^ set2
print(f"Symmentrical Difference using ^ :",symmentric_difference_result)


# Find using symmentrical_difference
print(f"Symmentrical Difference using method:",set1.symmetric_difference(set2))

""" 
5. MEMBERSHIP TEST
CHECKS IF A PARTICULAR ITEM EXISTS IN A SET
"""