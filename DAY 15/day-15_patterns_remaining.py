"""
6th August 2025
Practice Day

"""

#2. Alphabetical Patterns

#1. Example 1: Right Angled Triangle
rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    
"""
OUTPUT:
A
A B
A B C
A B C D
A B C D E

"""

#2. EXAMPLE 2 : INVERTED RIGHT ANGLED TRIANGLE

r = 5
for i in range(1,r+1):
    for j in range(r,0,-1):
        print(chr(64+j),end=" ")
    print()
    
"""
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
"""
r= 5
for i in range(r,0,-1):
    a=1
    for j in range(1,i+1):
        print(chr(64+a),end=" ")
        a+=1
    print()
    
"""
A B C D E
A B C D
A B C
A B
A

"""

#3. Left Aligned right angled triangle
rows = 5
for i in range(1,rows+1):
    print(" "*(rows - i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

"""
    A
   A B
  A B C
 A B C D
A B C D E
"""

#4. Square Pattern Alphabets
rows = 5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(chr(64+j),end=" ")
    print()

"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""

#5. Rectangular Pattern (4*6)
row =5
for i in range(1,rows):
    for j in range(1,rows+2):
        print(chr(64+j),end=" ")
    print()
    
"""
A B C D E F
A B C D E F
A B C D E F
A B C D E F
"""

#6. Example : Aphabet Pyramid Pattern

for i in range(1,row+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    

# Example 7 : Diamond Pattern

rows =5
#top part
for i in range(1,row+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    
#bottom part
for i in range(rows-1,0,-1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()


# Example 8 : Hollow Sqaure Alphabet Pattern
rows = 5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or j==rows:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
    
# Example 9: Repeated Character Triangle 
a=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+a),end=" ")
    a+=1
    print()
    
"""
A
B B
C C C
D D D D
E E E E E

"""

#10. Example 10: Alphabet Floyd's Triangle
ch=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+ch),end=" ")
        ch+=1
    print()
    
"""
A
B C
D E F
G H I J
K L M N O

"""

"""

3. Special SYMBOL PATTERNS

"""

#1. EXAMPLE 1 : RIGHT ANGLED STAR PATTERN

"""
$
$ $
$ $ $
$ $ $ $
$ $ $ $ $
>>>

"""
row1 =5
for i in range(0,row1):
    for j in range(0,i+1):
        print("$",end=" ")
    print()
    

#2. Inverted @ triangle
"""
@ @ @ @ @
@ @ @ @
@ @ @
@ @
@

"""
for i in range(row1,-1,-1):
    for j in range(i):
        print("@",end=" ")
    print()
    
# Example 3: Right Aligned Triangle #

for i in range(row1):
    print(" "*(row1-i-1),end="")
    for j in range(i+1):
        print("#",end=" ")
    print()
   
"""
    #
   # #
  # # #
 # # # #
# # # # #

""" 
    
# EXAMPLE 4 : Hollow Square

"""
& & & & &
&       &
&       &
&       &
& & & & &

"""
for i in range(1,row1+1):
    for j in range(1,row1+1):
        if i==1 or i ==row1 or j==1 or j==row1:
            print("&",end=" ")
        else:
            print(" ",end=" ")
    print()
    

# EXAMPLE 5: Left Aligned Increasing % Triangle
row_left = 5
for i in range(1,row_left+1):
    print(" % "*i)
    
"""
 %
 %  %
 %  %  %
 %  %  %  %
 %  %  %  %  %"""

 
 # Example 6: Left Aligned Decreasing Triangle
 
for i in range(row_left,0,-1):
    print("! "*i)
    
"""
! ! ! ! !
! ! ! !
! ! !
! !
!

"""

# Example 7: Pyramid of Symbols
for i in range(1,row_left+1):
    print(" "*(row_left-i)+"^ "*i)
    
"""
    ^
   ^ ^
  ^ ^ ^
 ^ ^ ^ ^
^ ^ ^ ^ ^
"""

     
# Example 8 : Diamond Pattern (+)

for i in range(1,row_left+1):
    print(" "*(row_left-i)+"+ "*i)
for i in range(row_left-1,0,-1):
    print(" "*(row_left-i)+"+ "*i)
    
    
# EXAMPLE 9 : Cross Pattern [ Doubt]
rows =5
for i in range(rows):
    for j in range(rows):
        if i==j or i+j==rows -1:
            print("~",end=" ")
        else:
            print(" ",end="")
    print()
        
        
# Example 10 : HolloW Diamond

"""
4. Star Patterns

"""

#1. Right Angled Triangle
row_left = 5
for i in range(1,row_left+1):
    print("* "*i)
    
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
"""
*
* *
* * *
* * * *
* * * * *
"""

#2. Right Angled Triangle
rows = 5
for i in range(1,rows+1):
    print(" "*(rows -i)+"* "*i)
    
for i in range(1,6):
    print(' '*(rows-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()
    
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

for i in range(3):
    print(" ")

#3. Inverted right angled triangle
for i in range(5,0,-1):
    print("* "*i)

  
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
        
        
#4. Inverted Right Angled Triangle
r= 5
for i in range(r,0,-1):
    print(" "*(r-i)+"* "*i)
    
"""
* * * * *
 * * * *
  * * *
   * *
    *
    
    """
    
#5. Pyramind Pattern
rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i)+"* "*i)
    
"""
    *
   * *
  * * *
 * * * *
* * * * *

"""

#6. Inverted Pyramid
r = 5
for i in range(r,0,-1):
    print(" "*(r -i)+"* "*i)
    
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

#7. Diamond Pattern
rows =5
# top half
for i in range(1,rows+1):
    print(" "*(rows-i)+"* "*i)
# bottom half
for i in range(5-1,0,-1):
    print(" "*(rows-i)+"* "*i)
    
"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
    
    """
    
# Hollow Rectangle
rows = 5
cols = 7
for i in range(1,5+1):
    for j in range(1,cols+1):
        if i==1 or i== 5 or j==1 or j==cols:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  
"""

* * * * * * *
*           *
*           *
*           *
* * * * * * *

""" 

#9. Hour Glass Pattern
r=5
for i in range(r,0,-1):
    print(" "*(r-i)+"* "*i)
    
# hour glass bottom part
for i in range(1,6):
    print(" "*(r-i)+"* "*i)
    
"""

* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *

"""

#10. Hollow Pyramid Pattern
r = 5
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="")
    for k in range(r-i+1):
        print("*",end=" ")
    print()