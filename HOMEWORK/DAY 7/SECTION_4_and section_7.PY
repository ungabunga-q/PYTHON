"""
TUPLE: OPERATIONS

1. CONCATENATION
2. REPETITION
3. MEMEBERSHIP TEST
4. COUNT OCCURANCE
5. INDEX OF ELEMENT
6. NESTED
7. TUPLE UNPACKING
8. LEN()

"""

#1. TUPLE CONCATENATION
t1 =("Pen",'Pencil')
t2 =("Eraser",)
stationery = t1+t2;print(stationery)


#2. tuple repetition
greet =("Hii",);print(greet*3)

#3. Membership Test
skills =("Python",'sql','excel')
print('sql' in skills)


#4. Count occurance
nums =(1,2,3,2,4,2,5,2)
print(nums.count(2))

#5. Index of element
animals =('cat','cow','dog','dog')
print(animals.index('dog'))

#6. Convert list to tuple
items =['apple','cherry','banana']
print(tuple(items))


#7. Tuple unpacking
product =('Laptop',55000,'kiwi')

name,price,category = product
print(f"Name is {name} of this {category} category priced {price}")

#8. Nested tuple access
employees =(('Rahul','HR'),('Shalini','IT'))
print(employees[0][1])

#9. Iterate with index
fruits =('Mango','Guava','Grapes')
for i in range(len(fruits)):
    print(f"Fruit {i+1}: {fruits[i]}")

#10. Using len function
colors =('Red','Blue','Orange')
print(len(colors))


#11. Combine tuples with numbers
t1 =(1,2);t2=(3,4);result = t1+t2
print(result)

#12. get all even numbers from tuple
numbers = tuple(range(1,7))
evens = tuple(i for i in numbers if i%2==0);print(evens)

#13. Convert string to tuple
msg="Hello"
t_msg = tuple(msg);print(t_msg)

#14. Sorting a tuple
unsorted_t =(4,6,1,2,86,34,1,4);s_t =sorted(unsorted_t)
print(s_t)

#15. Remove duplicates
data =(1,2,2,3,4,5,6,5,5,5)
unique_data = tuple(set(data))
print(unique_data)

#16. Reverse a tuple
tuple_2 = ('a','b','c')
print(tuple_2[::-1])

#17. Convert tuple to string
words =("Hello","World")
sentence = " ".join(words);print(sentence)

#18. Compare two tuples
a =(1,2,3);b=(1,3,50)
print(a > b)

#19. tUPLE IN A DICTIONARY KEY





"""
SECTION 7: 
TUPLE OPERATIONS

"""