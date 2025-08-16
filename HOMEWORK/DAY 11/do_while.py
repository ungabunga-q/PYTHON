"""
DO WHILE PRACTICE

"""

#1. Ask age until valid
while True:
    age =int(input("Enter your age:"))
    if age >0:
        break
    
#2. Email Validation
while True:
    email=input("Enter email")
    if '@' in email:
        print("Valid Email")
        break
    
    
#3. Ask for movie rating between 1-5
while True:
    rating = int(input("Enter rating between 1-5: "))
    if 1<=rating<=5:
        print(f"You rated {rating}")
        break
    
#4. Accept terms and conditions
while True:
    t_c =input("Enter terms and conditions yes/no: ")
    if t_c.lower() =='yes':
        print("Order Placed")
        break
    
#5. Confirm food order
while True:
    food =input("Enter food order: yes/no ")
    if food.lower() =='yes':
        print("Order placed food")
        break
    
#6. Ask name with atleast three characters
while True:
    name =input("Enter your name: ")
    if len(name)>=3:
        print("Input accepted Successfully")
        break
    
#7.Select correct menu option
lst=['Start Game','Exit','Choose']
print("List of Options :")
for i in range(len(lst)):
    print(f"{i+1} : {lst[i]}")
while True:
    option = int(input("Enter option here: "))
    if option ==2:
        print("Exiting")
        break
    

#8. Ask for integer only
while True:
    try:
        in_put= int(input("Enter integer only: "))
        break
    except ValueError:
        print("Enter integer only:")
        
        
    