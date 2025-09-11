"""
POLYMORPHISM
PRACTICE SET

"""
# Basic Examples

# METHOD OVERLOADING

# 2. Greet Function
def greet(name,mag='Hello'):
    print(f"{mag} , {name}")
    
greet("Aishwarya")
greet("Aishwarya","Good Morning")


# 3. Shopping Discount
def discount(price,percent=0):
    return price - (price*percent/100)

print("Price after discount",discount(1000))
print("Price after 20% discount",discount(1000,20))

#4. Travel Booking (optional seats and destination)
def book_tickets(name,seats=1,destination="Delhi"):
    print(f"{name} booked {seats} seat(s) to {destination}")
    
    
book_tickets("Aishwarya",2,"Goa")
book_tickets("Shalini",2,"Mumbai")

#5. Student Grade ( marks optional)
def grade(name,marks=None):
    if marks is None:
        print(f"{name}'s grade is pending")
    else:
        print(f"{name}'s grade is based on marks {marks}")
        
        
grade("Jay")
grade("Kavita",85)

# Operator Overloading
class Vector:
    def __init__(self,x,y):
        self.x= x
        self.y =y
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    
    def __str__(self):
        return f"{self.x} , {self.y}"
    
v1,v2 =Vector(2,5),Vector(4,-1)
print(v1+v2)

# 3. String repetition with "*"
class Repeat:
    def __init__(self,text):
        self.text = text
        
    # overloading
    def __mul__(self,n):
        return self.text*n
    
r = Repeat("Hii")
print(r.__mul__(5 ))

print(r*3)

#4. Comparing students by marks using >
class Student:
    def __init__(self,name,marks):
        self.name,self.marks=name,marks
        
    def __gt__(self,other):
        return self.marks > other.marks
    
s1,s2 = Student('a',85),Student('b',90)
print(s1>s2)
s1.__gt__(80)
    
    
# 5. Custom Length using len()

class Team:
    def __init__(self,members):
        self.members = members
        
    def __len__(self):
        return len(self.members)
    
    
t = Team(['A','B','C'])
t.__len__()
print(len(t))
    
    
        
        
    
    
    
