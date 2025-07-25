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
    
#10. File existence
file_exists = False
if file_exists:
    print("File found")
else:
    print("File not found")
    
    
#3. elif (Else if ) Statement

"""
Definition:
Allows checking multiple conditions sequentially after an initial if
Syntax:
if condition1:
        # block1
elif conditional2:
        # block2
elif conditional3:
        # block3
else:
    # default block
    
Purpose:
To handle mutliple possible outcomes with clear priority.
"""
# Examples

#1. Greeting based on time
time = 18
if time <12:
    print("Good Morning")
elif time < 17:
    print("Good Afternoon")
else:
    print('Good Evening')
    

#2. Grade System
marks = 65
if marks >=90:
    print("A grade")  
elif marks >=75:
    print("B grade")
elif marks >=60:
    print("C Grade")
else:
    print("D grade")

#3. Weather message
temp = 5
if temp> 30:
    print("Hot")
elif temp > 20:
    print("Warm")
elif temp > 10:
    print("Cool")
else:
    print("Cold")
    
#4. BMI
bmi = 28
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
    
#5. Membership Level
points = 300

"""
Nested if Statement:

Definition:
Placing an if statement inside another if block.

Syntax:
if outer_condition:
            if inner condition:
                        #nested block
                        
                        
                        
Purpose:
To check multiple related conditions hierarchically.

"""

#1. Job eligibility 
age = 25
degree ='Bachelor'
if age >=18:
    if degree=="Bachelor":
        print("Eligible for job")

#2. Purchase decision
price = 800
budget = 1000
if budget >=price:
    if price > 500:
        print("Purchase with discount")
    else:
        print("Purchase without discount")
        
        
#3. Exam pass with grace
marks = 38
if marks <40:
    if marks >=35:
        print("Marks with grace marks")
    else:
        print("Fail")
        

#4. File Operations
file_open = True
file_type ='text'
if file_open:
    if file_type=='text':
        print("Read text file type")
        
#5. Security Check
is_logged_in = True
is_admin = True
if is_logged_in:
    if is_admin:
        print("Admin panel access")
    else:
        print("User panel access")