"""
In Python,patterns are often created using nested loops.


1. Outer loop controls row
2. Inner Loop controls columns / elements in a row.
3. print() is used with end="" to control spacing and avoid newline
4. print() -> Moves to the next line after each row


There are multiple types such as:

1. Number patterns
2. Alphabetical Patterns
3. Special Symbol Patterns
4. Star Patterns

"""

#1. Number Pattern
""" n = int(input())
for i in range(1,n):
    for j in range(1,n-i):
        print(j,end="")
    print()
     """

"""
...
123
12
1
"""

rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# Example 2: Inverted right angled triangle

rows = 5
for i in range(rows,0,-1): #Outer loop for each row
    for j in range(1,i+1): #Inner Loop for 1 to i
        print(j,end=" ") # Print numbers from 1 to i
    print()  # New line after each row
    
    
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

#3. Left aligned right angled triangle

rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")  # print spaces for left alignment
    for j in range(1,i+1):  #print numbers from 1 to i
        print(j,end=" ")    # Newline after each row
    print()
    
"""
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""

# Example 4: Square number pattern

rows = 5
for i in range(1,rows+1): #rows from 1 to 5
    for j in range(1,rows+1): #columns from 1 to 5
        print(j,end=" ")  # print numbers from 1 to 5
    print()               # Newline after each row
    
    
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""

# 5. Rectangle pattern (4x6)
for i in range(4):             # 4 rows
    for j in range(1,7):       #6 columns
        print(j,end=" ")       # Print from 1 to 6
    print()    # Newline after each row
    
"""
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6

"""

# Example 6: Pyramid Number Pattern
rows = 5
for i in range(1,rows+1):                  #padding for centering
    print(" "*(rows-i),end="")     # print numbers from 1 to i
    for j in range(1,i+1):
        print(j,end=" ")        #newline after each row
    print()
    
"""
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""

# Example 7: Diamond number pattern
# top half
rows = 4
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    

for i in range(rows-1,0,-1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
"""
   1
  1 2
 1 2 3
1 2 3 4
 1 2 3
  1 2
   1
   
   """
   
#8. Hollow Square Numbers
rows = 5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        # prints rows or columns border 
        if i ==1 or i == rows or j==1 or j==rows:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
#9. Pascal Triangle
rows = 5
for i in range(rows):
    num = 1
    print(" "*(rows -i),end="")
    for k in range(i+1):
        print(num , end=" ")
        num = num*(i-k)//(k+1)
    print()
    
    
# Example 10: Floyd's Triangle
rows = 5
num = 1
for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num +=1
    print()
    
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
    