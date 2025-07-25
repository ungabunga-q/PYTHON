"""
You can create dictionary using different techniques.

{} -literal
dict()- constructor
zip()- Function
Dictionary Comprehension
Tuples/Lists

"""

#1. Using dict() constructor
user = dict(name='Anil',age=24)
print(user)


#2. From a list of tuples
employees = [('name','Rita'),('age',30)]
employees_dict = dict(employees)
print(employees_dict)

#3. Using zip function 
keys =['Maths','Science'];values =[90,95]
a = dict(zip(keys,values));print(a)


#4. Comprehension

squares ={i:i**2 for i in range (1,50,3)}
print(squares)


#5. From two lists
names =['A','B','C'];scores =[80,85,90]
students =dict(zip(names,scores))
print(students)

#6. Nested using dict()
nested = dict(A =dict(x=1),B=dict(y=2))
print(nested)


#7. Default Value for list Comprehension
default ={ k:0   for k in ['a','b','c']}
print(default)

#8. Character count using Comprehension
string_data ="Hello WORLD ,How are you?When are you going to study?"

string_data_dict ={ i:string_data.count(i) for i in string_data}
print(string_data_dict)

#9. Using Range Keys
range_dict ={ i:chr(65+i) for i in range(5)}
print(range_dict)


#10. Key from Tuple List
t_list =[('x',10),('y',20)]
t_dict =dict(t_list)
print(t_dict)


#11. Boolean Keys
b_dict ={True:'yes',False:'no'}
print(b_dict)


#12. 