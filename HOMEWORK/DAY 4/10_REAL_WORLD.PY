"""
REAL WORLD PYTHON PROBLEMS

"""

#1. Sum of two numbers
a = int(input("Enter first number:"))
b = int(input("Enter 2nd number:"))
sum = a+b;print(sum)

#2. Area of circle
# Calculate the area of a circle given its radius
r = int(input("Enter the radius of the circle"))
area = (r**2)*3.14
print(area)

#3. Swap two numbers
# Swap two numbers
a1 = int(input("Enter 1st number"))
b1 = int(input("Enter 2nd number:"))
print(f"Before Swapping {a1} and {b1}")
a1,b1=b1,a1
print(f"AFTER  Swapping {a1} and {b1}")


#4. Check even or odd number
e_o = int(input("Enter a number:"))
if e_o %2==0:
    print("Even number")
else:
    print("Odd Number")



#7. Find largest number of two numbers
a_b = int(input("Enter a number "))
b_a = int(input("Enter a number "))
if a_b > b_a:
    print(f"{a_b} is greater than {b_a}")
else:
    print(f"{b_a} is greater than {a_b}")
    
    