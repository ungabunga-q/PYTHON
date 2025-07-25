"""
IMMUTABILITY

"""

#1. TRYING TO MODIFY TUPLE ELEMENT
person =('Amit',30)
#person[1] = 25


#2. Using try-except to show immutability

try:
    person[0] = 'Rahul'
except TypeError as e:
    print("Error: ",e)

#3. Appending to tuple not allowed
t =(1,2,3)
#t.append(4)

#4. Deleting tuple element  not allowed
#del t[2]

#5. Using replace like behavior
person =('John',25)
person =(person[0],26)
print(person)

#6. Tuples inside a list can be changed by replacing tuple
data =[('Alice',1),('Bob',2)]
data[0] =('Alice',3)
print(data)


#7. Elements can't be popped
#t.pop()

#8. You can slice but cannot modify
print(t[:2])

#9. Concatenation
t1=(1,2);t2=(3,); t =t1+t2
print(t)

#10 .Tuples are hashable  #doubt
coordinates = (10,20)
print(hash(coordinates))

#11. Use tuple in set
unique = {(1,2),(3,4)}
print((1,2) in unique)

#12. Tuple values fixed in functions
#doubt

#13. Protect values using tuples
api_keys =('key123','key456')
print(api_keys)

#14. Tuple inside list - modidy list not tuple
student =[('Ravi','BCA')]
student[0] =('Ravi','MCA');print(student)

#15. Strings are immutable like tuples  #doubt
msg ="Hello"
try:
    msg[0]='H'   
except TypeError:
    print("Immutable")
    
    
#16. Tuple with mutable elements (not safe)

t_m =([1,2],[3,4])
t_m[0][0]=100;print(t_m)

#17. Immutable record storage 
record =('ID001','Shalini','Trainer')
print(record)

#18. Attempt to add new element
#record.append("New")

# 19. Use tuple in caching/frozen state
cached_data = ("User123", "Page5")
print("Cached:", cached_data)


#20. Tuple in function default arguement
def greet(info=("Guest",)):
    print(f"Hello {info[0]}")
    
greet()




#21. Replacing tuple requires reassignment
address =("Delhi","India");address =("Mumbai","India")
print(address)

#22. Check immutability of data
data =(10,20);print(isinstance(data,tuple))

#23. ID CARD INFO
id_card =("AISHWARYA","MUMBAI","DATA ANALYST");print(id_card)

#24. IMMUTABLE TIMESTAMPS
Timestamp =(2025,7,12,16,30);print(Timestamp)

#25. Tuple values in loops can't change
status =("Active","Blocked")
for s in status:
    print(s.upper())
    
print(status)