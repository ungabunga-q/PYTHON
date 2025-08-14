"""
LOOP STATEMENTS

# Loops are used to execute a block of code repeatedly for a 
# specified number of items


"""

num1,num2,num3,num4,num5=1,2,3,4,5
print(num1);print(num2);print(num3);print(num4);print(num5)

"""
While Loop --> The while loop continues executing a block as long as 
the condition is True.

Syntax:

while condition:
        #block of code

"""

for i in range(1,6):
    print(i)
    

# Examples:

#1. Print numbers from 1 to 5
i =1
while i<=5:
    print(i)
    i+=1
    
    
# Example 2: Print numbers less than 10
num  = 2
while num < 10:
    print(num)
    num+=2
    
# Example 3: Sum of numbers till 100
sum=0
i=1
while i<=100:
   sum+=i
   print(i,sum)
   i+=1
   
print('Total till 100',sum) 

""" l=[]
for i in range(1,101):
    l.append(i)
print(l)
print(a =sum(l)) """



#Example 4: Count Down Timer
count =5
while count>0:
    print(count)
    count-=1
    
    
# Example 5: Validating User Input
user_input =""
while user_input !='yes':
    user_input=input("Type yes to continue:")
    
    
"""

2. Simulated do while loop (Python doesn't have built in do while)

A do-while loop executes the block atleast once and then checks the condition.
If the condition is False,it stops the loop.

Syntax: Simulated using while True and BREAK
"""

# Examples:
# Example 1: Print number once, then check
i=1
while True:
    print(i)
    if i>=5:
        break
    i+=1
    
# Example 2: User Password Input Validation
while True:
    password = input('Enter password')
    if password =='admin':
        print("Access Granted")
        break
    
#3. Menu Simulation
while True:
    print("1. Start\n2.Exit")
    choice =input('Enter Choice:')
    if choice=="2":
        break
    
    
#4. Sum input until 0
while True:
    num =int(input("Enter number [0- to stop]"))
    if num==0:
        break
    
    
# Example 5: Print even numbers till 10
i=0
while True:
    i+=2
    print(i)
    if i>=10:
        break
    
    
"""
For Loop : A for loop is used to iterate over a sequence
[like lists, tuples,string , range,dictionary etc...]

Syntax:
for variable in sequence:
                block
                

"""

# 1. Print numbers from 1 to 5
for i in range(1,6):
    print(i)
    
    
#2. Print characters into a string
for char in "Python":
    print(char)
    

#3. Sum of numbers using for loop
total =0
for i in range(101):
    total+=i
print("Sum : ",total)


#4. Print table of 3
for i in range(11):
    print(f"3*{i}={3*i}")
    
#5. Countdown of 5
for i in range(5,0,-1):
    print(i)
    
"""
4. For loop iterating over collections 

"""
fruits =['apple','banana','cherry']
for fruit in fruits:
    print(fruit)
    
    

# Example 2: Dictionary keys and values
person ={'name':'John','age':25}

for key,value in person.items():
    print(key," : ",value)
    
    
# Example 3: Set elements
colors ={'red','blue','green'}
for color in colors:
    print(color)
    
# Example 4: Tuple Iteration
nums =(10,20,30)
for num in nums:
    print(num)
    
    
# EXAMPLE 5: Iterating over string
for ch in 'Hello World':
    print(ch)
    
    
"""
5. NESTED LOOPS

A loop inside another loop.
Useful for grids, patterns , matrices etc.....

"""

#1. Print Matrix
for i in range(3):
    for j in range(3):
        print(i,j)
    print()

#2. Multiplication Table
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}*{j}={i*j}")
    print()
    

#3. Star Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
#4. Number grid
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()
    
    
#5. Nested List Process
matrix=[[1,2],[3,4],[5,6]]
for row in matrix:
    for val in row:
        print(val)
        
        
"""
6. Break Statement

"""
#1. Stop loop at 5

for i in range(10):
    if i==5:
        break
    print(i)
    
    
#2. While loop break
i =1
while True:
    if i>3:
        break
    print(i)
    i+=1
    
    
    
#3. Loop user input until 'exit'

while True:
    cmd = input('Type exit to stop: ')
    if cmd=='exit':
        break
    
    
#4. Stop on negative number
nums =[1,2,3,-1,4]

for ele in nums:
    if ele<0:
        break
    print(ele)
    
#5. Break in nested loop
for i in range(3):
    for j in range(3):
        if j==2:
            break
        print(i,j)