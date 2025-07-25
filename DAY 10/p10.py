"""
Control Structure:
Control Structures let you control the flow of execution in your program.
They decide which block of code  runs, depending on coditions.
As - If, If- Else, elif, nested, etc....


Indentation:
Python uses indentation ( spaces or tabs) to define block-level structure
instead of curly braces {} (like in C/C++/Java).

Convention: 4 spaces per indentation level

Example:
IF condition :
        # indented block run if condition is True

"""

#1. Simple if statement
"""
Definition: Executes a block of code only if the condition is true.

Syntax:
If condition:
            # STATEMENTS

Purpose:
To perform an action when a condition is met.

"""

# Examples:

#1. Check Temperature
temp = 32
if temp >30:
    print("Its a hot day!")
    
    
#2. Check bank balance
balance = 1000
if balance >=500:
    print("Sufficient funds")
    
#3. Check driving age
age = 20
if age >=18:
    print("You can drive")
    
    
#4. Door sensor
door_open = True
if door_open:
    print("Door is open")
    
#5. Rain Check
is_raining = False
if not is_raining:
    print("You need an Umbrella")
    
    
#6. Admin Check
user_role="admin"
if user_role =='admin':
    print("Access Granted.")
    
    
#7. High Score
score = 95
if score >90:
    print("You got a high score")
    
#8. Room Temperature
room_temp =25
if room_temp < 30:
    print("Room temperature is comfortable")
    
    
#9. Morning Check
hour = 7
if hour < 12:
    print("Morning time it is ")
    
#10. Stock Price
stock_price = 120
if stock_price > 100:
    print("Stock price is above target")
    
    
#2. If else statement

"""
Definition:
Executes one block if condition is true,otherwise executes another block.

Syntax:
if condition:
            #true block
else:
            #false block
 
Purpose:
To handle two mutually exclusive outcomes.           


"""

# Examples:

#1. Pass/Fail
marks = 45
if marks >=40:
    print("Pass")
else:
    print("Fail")


#2. Login Success
username ='user'
if username=='admin':
    print("Welcome, admin!")
else:
    print("Unknown user")
    
    
#3. Light Switch
light_on = False
if light_on:
    print("Light is on")
    
#4. Attendance
present = True
if present:
    print("Marked present")
else:
    print("Marked Absent")
    
    
#5. Battery Level
battery=10
if battery <20:
    print("Low Battery warning")
else:
    print("Battery is okay")
    

#6. Exam eligibility
attendance_percentage =80
if attendance_percentage >=75:
    print("Eligible for exam")
else:
    print("Not eligible for Exam")
    
    
#7. Payment status
payment_done = True
if payment_done:
    print("Payment Successful")
else:
    print("Payment Pending")
    
#8. Seat Availability
seats =0
if seats >0:
    print("Seats Available ")
else:
    print("Sold out")
    
    
#9. Discount Offer
purchase_amount = 300
if purchase_amount > 500:
    print("Discount Applied")
else:
    print("No discount")
    
