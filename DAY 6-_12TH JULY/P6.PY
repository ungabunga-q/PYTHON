#------------------------- LIST ----------------------------

# DEFINING A LIST
"""
A list is a collection of items enclosed in a square brackets [].
Lists are ordered, mutable, and can be heterogenous data.
A list is a built-in data structure in Python.

Lists are:
1. Ordered: The positions of the items are fixed.
2.Mutable: We can change the elements after creating the lists.
3.Heterogeneous : Can hold items of different types (int, str, bool,etc..)
4. Defined using square brackets.


"""

#1. A list can hold different types of elements
my_list = [10,"Python",3.14,True]

#2. LIST OF INTEGERS
numbers =[1,2,3,4,5]

#3. list of strings
fruits = ["apple","banana","cherry"]

names =["Pigarori","Purpur","Puchki"]

# 4. Empty List
empty =[]

#5. Lists containing other lists (nested list)
nested_list = [[1,2],[3,4]]
print(nested_list[0][1])

#Creating list
# You can create a list  using brackets or the list constructor

#1. Example: Using []
colors =["Red","Green","Blue"]

#2. Example: Using list()
letters = list("Python");print(letters)

#3. Create a list from a range
num =list(range(1,7));print(num)

#4. Repeating elements
zeros = [0]*5;print(zeros)
print([1,2,3]*5)

#5. List from another iterable
data = list((10,20,30));print(data)

# Accessing list elements of list
#use Indexing ([]) and slicing ([:]) to access list elements.

#1. Indexing
fruits1 = ["Apple","Banana","Cherry"]
print(fruits1[0])  #apple

#2. Negative indexing
print(fruits1[-1])  #cherry

#3. Slicing 
print(fruits[0:2]) #["Apple","Banana"]

# 4. Full List
print(fruits[:])

# 5. Access Nested List
nested_list= [[1,2],[3,4]]
print(nested_list[1][0])


# LISTED METHODS 
"""
Common methods to modify or work with lists:
append() – adds an element to the end of the list
clear() – removes all elements from the list    
count() – returns the number of occurrences of a value in the list
extend() – adds multiple elements to the end of the list
index() – returns the index of the first occurrence of a value in the list
insert() – inserts an element at a specified position in the list
pop() – removes and returns an element at a specified position in the list
remove() – removes the first occurrence of a value in the list
sort() – sorts the list in ascending order
reverse() – reverses the order of the list

[append,insert,remove,pop,extend] ----------> mam mentioned
"""
#1. Append()
items =[1,2];items.append(3);print(items) #[1,2,3]
item =[1,2,3];item.append([6,7,8,9,10]);print(item)

#2. INSERT()
items.insert(1,"a") ; print(items)  #[1,a,2,3]

#3. Remove()
items.remove('a')  #removrs a results [1,2,3]
print(items)

#4. pop()
items.pop(1) ; print(items) #[1,3]
items.pop()

#5. extend()
items.extend([4,5])
print(items) #[1,3,4,5]


#Functions used with list
""" 
Built-in functions are used to analyze list contents.

len() - Length of the list
max() -Maximum value
min() - Minimum value
sum() - Sum of all elements
sorted() - Returns a sorted copy

"""
nums =[10,5,30,25]

#1. Length()
print(len(nums))  #4

#2. Max()
print(max(nums))  #30

#3. min()
print(min(nums))  #5

#4. Sum()
print(sum(nums)) #70

#5. sorted()
print(sorted(nums))  # [5,10,25,30]

""" 
SORTING A LIST:
THERE ARE TWO WAYS TO SORT A LIST:

1. SORT() - SORTS A LIST IN PLACE (MODIFIES ORIGINAL LIST)
2. SORTED() - RETURNS A NEW SORTED LIST  ( ORIGINAL STAUS UNCHANGED)

"""

# 1. Ascending Sort
marks =[85,92,75,60];marks.sort();print(marks)

#2. descending Sort
marks.sort(reverse=True);print(marks)


#3. Sorted()
scores =[33,11,44];print(scores)
new_scores =sorted(scores);print(new_scores)

#4. Sort Strings
names =["Jay","Mahi","Amit"]
names.sort();print(names)

#5. Sort mixed cases
words =["banana","Apple","cherry"];print(sorted(words))

