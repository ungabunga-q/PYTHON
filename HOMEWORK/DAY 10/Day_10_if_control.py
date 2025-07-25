"""
SECTION 1: SIMPLE IF STATEMENTS

"""

# 1. Is dataset empty
data_rows =0
if data_rows ==0:
    print("Dataset is empty")
    
    
#2. Check if feature exists
feature ='price'
columns =['id','name','price']
if feature in columns:
    print("Feature found in dataset")
    
#3. Outlier Check
value =1000
if value > 500:
    print("Potential Outlier")
    
#4. Server Health
cpu_usage = 85
if cpu_usage > 80:
    print("High CPU Useage")
    
#5. Is string empty
input_text =""
if input_text=="":
    print("No input provided")
    
#6. API Response Check
status_code = 200
if status_code==200:
    print("API Call Successful")
    
    
#7. File Extension Pack
filename ='report.csv'
if filename.endswith('.csv'):
    print("CSV File Detected")
    
#8. DataFrame Shape Check
rows = 1000
if rows > 500:
    print("Large Dataset Loaded")
    
#9. Connection Active
is_connected = True
if is_connected:
    print("Database connected")
    
#10. Memory Useage
ram =90
if ram >=90:
    print('Memory almost full')
    
    
#11. Weekend Check
day ='Sunday'
if day in ['Saturday','Sunday']:
    print('IT is the weekend')
    
#12. Feature Importance Threshold
importance = 0.1
if importance <0.05:
    print("Feature not important")
    
#13. Model Accuracy
accuracy = 0.95
if accuracy >0.9:
    print("Model is highly accurate")
    
#14. Check permission
role='developer'
if role=='admin':
    print('Full permission granted')
    
#15. Browse detection
browser ='Chrome'
if browser=='Chrome':
    print("Optimised for Chrome")
    
#16. Password Length
password ='pass123'
if len(password) <8:
    print("Password too short")
    
#17. Email Validation

email='test@example.com'
if '@' in email:
    print("Email looks Valid")
    

#18. Enviornment Type
env ='production'
if env == 'production':
    print("Running in production")
    
    
#19. Data Type Check
var = 5.5
if isinstance(var,float):
    print("Variable is Float")
    
    
#20. Loop Counter
i=10
if i%2==0:
    print("Even Index")
    
    
#21. API TOKEN PRESENCE
token =None
if token == None:
    print("API Token Missing")
    
    
#22. String Match
username='Admin'
if username.lower()=='admin':
    print("Admin user detected")
    
    
#23.  Data point Value
temperature = -5
if temperature < 0:
    print('Freezing Temperature')
    
    
#24. Disk Space
disk_free = 15
if disk_free < 20:
    print(F"Your disk is full. Almost {disk_free}% is remaining.")
    
    
#25. Time Format
time_str='14:30'
if ':' in time_str:
    print("Valid Time Format")
    
    
#26. Character in text
msg='Hello, World!'
if '!' in msg:
    print("Exclamatory Message")
    
#27. Feature Enabled
feature_flag = False
if not feature_flag:
    print("Feature Disabled")
    
    
#28. Deprecated API Usage
api_version ='v1'
if api_version =='v1':
    print("Deprecated api version used")
    
    
#29 . Integer Check
number =100
if isinstance(number,int):
    print("Variable is integer")
    
#30. Login ATTEMPT
attempts = 3
if attempts >2:
    print("Too many login attempts")
    
    
    
"""
PRACTICE: IF ELSE EXAMPLES
(30 EXAMPLES)

"""
#1. Data source availability
source_online = False
if source_online:
    print("Source Online")
else:
    print("Source Offline")
    
    
#2. Data upload status
upload_success = True
if upload_success:
    print("Upload completed")
else:
    print("Upload Failed")
    
#3. Uset active status
active = False
if active:
    print("User is active")
else:
    print("User inactive")


#4. Password Match
password ='1234'
confirm ='abcd'
if password==confirm:
    print("Password match")
else:
    print("Password do not match")
    
#5. SSL enabled
ssl = True
if ssl:
    print("Secure Connection")
else:
    print("Insecure connection")
    
    
#6. LOGIN LIMIT
login_today =4
if login_today < 5:
    print("You can login today")
else:
    print("lOGIN LIMIT EXCEEDED")
    
    
#7. Data saved confirmation
saved = False
if saved:
    print('Data Saved')
else:
    print('Failed to saved the data')
    
    
#8. Is Image Grayscale
channels =1
if channels==1:
    print("Image is Grayscale")
else:
    print("Image is coloured")
    
    
#9. Meeting Duration
duration =55
if duration <=60:
    print("Meeting within time")
else:
    print("Meeting overtime")
    
    
#10. Temperature alert
temp = 38
if temp > 37:
    print("Fever detected")
else:
    print('Temperature normal')
    
    
#11. DATABASE BACKUP

backup_done = True
if backup_done:
    print('Backup successful')
else:
    print("Backup Failed.")
    
    
#12. Even or odd ID
record_id = 567
if record_id%2==0:
    print("Even id")
else:
    print("Odd id")
    
#13. Subscription status
subscription_status = 'inactive'
if subscription_status=='active':
    print("You can watch now")
else:
    print("You need to pay to continue.")
    
    
#14. Folder exists
folder = True
if folder:
    print("Folder found")
else:
    print("Folder missing")
    
    
#15. Deployment Status
deployed = False
if deployed:
    print("Deployed complete")
else:
    print("Deployment Pending")
    
    
#16. Update Check
new_version = False
if new_version:
    print("Update Available")
else:
    print("Software up to date")
    
    
#17. User feedback
rating = 2
if rating >=4:
    print("Positive feedback")
else:
    print("Negative Feedback")
    
    
#18. Sensor triggered
sensor = True
if sensor:
    print("Motion detected")
else:
    print("No motion")
    
    
#19. Meeting slot available
slots =0
if slots >0:
    print("Slots available")
else:
    print("Not available")
    
#20. Test case result
test_pass = True
if test_pass:
    print("Test Passed")
else:
    print("Test Failed")
    
    
#21. Data Correction Needed
data_valid =True
if data_valid:
    print("No correction needed")
else:
    print("Data correction required")
    
    
#22. Download Complete
download =True
if download:
    print('Download Complete')
else:
    print("Download Failed")
    
#23. External API status
api_working =False
if api_working:
    print("External api working")
else:
    print("API DOWN")
    
    
#24. Encryption Check
encrypted =True
if encrypted:
    print("Data is encrypted")
else:
    print("Data is not encrypted")
    
#25. Payment completed
payment_done =True
if payment_done:
    print("Payment Successful")
else:
    print("Payment Failed")
    
    
#26. Password strength
password="123"
if len(password) >=8:
    print("Strong Password")
else:
    print("Weak Password")
    
    
#27. Notification on
notification = False
if notification:
    print("Notification enabled")
else:
    print("Notification disabled")
    

#28. Comment Moderation
approved = True
if approved:
    print("Comments Approved")
else:
    print("Comments rejected")
    
    
#29.  QR Code Scan
scanned = True
if scanned:
    print("QR code Scanned")
else:
    print("QR Code not Scanned")
    
    
#30. Day Light Mode
sunlight = False
if sunlight:
    print('Daylight mode active')
else:
    print("Night Mode on")
    
    
"""
IF-ELIF -ELSE LADDERS 
(30 EXAMPLES)

"""

#1. DATA VOLUME CHECK
## 750, 100,1000
records =750
if records <100:
    print("Small Dataset")
elif records <1000:
    print('Medium Dataset')
else:
    print('Large Dataset')
    
    
#2. Connection Speed
# 200,50,150
connection_speed =200
if connection_speed <50:
    print("Slow connection")
elif connection_speed < 150:
    print('Medium Connection')
else:
    print("Fast connection")
    
    
#3. Customer Loyalty
# 1500, 5000,2000,1000,
points_c=1500
if points_c >=5000:
    print("Diamond Customer")
elif points_c >=2000:
    print('Gold Customer')
elif points_c >=1000:
    print('Silver Customer')
else:
    print("Bronze Customer")
    
    
#4. User role privileges
#editor, admin,editor,viewer
role ="editor"
if role=="admin":
    print("Full Access Privileges")
elif role=='editor':
    print("Editing ACCESS")
elif role=='viewer':
    print("View Access")
else:
    print("No access")    
    
    
#5. Battery Health
battery_health = 80
if battery_health >90:
    print("Excellent")
elif battery_health >70:
    print("Good")
elif battery_health >50:
    print("Average")
else:
    print("Poor")
    
    
# 6. Quality Score
quality_score = 85
if quality_score >=95:
    print("Excellent Data")
elif quality_score >=80:
    print('Good Score')
elif quality_score >=60:
    print("Morderate Data")
else:
    print("Poor Data")
    
    
#7. Employee Expereince
years = 12
if years <2:
    print("Junior")
elif  years <5:
    print("Mid Level")
elif years <10:
    print("Senior")
else:
    print("Expert")
    
    
#8. Ticket Severity
severity ='critical'
if severity =='low':
    print("Low Priority")
elif severity=='medium':
    print("Medium Priority")
elif severity =='high':
    print("High Priority")
else:
    print("Critical Priority")
    
    
#9. Learning Progress
percent_complete = 45
if percent_complete < 25:
    print("Getting Started")
elif percent_complete < 50:
    print("In Progress")
elif percent_complete < 75:
    print("Almost there")
else:
    print("Completed ")
    
    
#10. Product Rating
rating =3
if rating==5:
    print("Excellent")
elif rating==4:
    print("Very Good")
elif rating==3:
    print("Good")
elif rating==2:
    print("Fair")
else:
    print("Poor")
    

#11. Weather Forecast
temp = 18
if temp >=35:
    print("Hot Day")
elif temp >=25:
    print("Warm Day")
elif temp >=15:
    print("Cool Day")
else:
    print("Cold Day")
    
    
#12. Response Time
response_ms =900
#100,500,1000

if response_ms <100:
    print('Instant Response')
elif response_ms <500:
    print('Fast Response')
elif response_ms <1000:
    print('Acceptable Response')
else:
    print('Slow Response')
    
    
#13. Bug Impact
user_affected =5000

if user_affected <100:
    print("Minor Issue")
elif user_affected <1000:
    print("Moderate Issue")
elif user_affected <10000:
    print("Major Issue")
else:
    print("Critical Issue")


#14. Disk Usage
disk_usage =85
if disk_usage <50:
    print("Low Useage")
elif disk_usage <75:
    print('Moderate Useage')
elif disk_usage <90:
    print('High Useage')
else:
    print('High Useage')
    
    
#15. Order Quantity
#120,50,100,500

order_quantity =120
if order_quantity <50:
    print('Small Order')
elif order_quantity <100:
    print('Medium Quantity')
elif order_quantity <500:
    print("Large Order")
else:
    print("Bulk Order")
    
    
#16. API Request Volume
requests_api = 800

if requests_api <100:
    print('Low Requests')
elif requests_api <500:
    print("Medium Requests")
elif requests_api <1000:
    print("High Requests")
else:
    print('Excessive Api Useage')
    
    
#17. Data Backup age
data_since_backup = 5
if data_since_backup <=1:
    print("Recent Backup")
elif data_since_backup <=7:
    print('Weekly Backup')
elif data_since_backup<=30:
    print("Monthly Backup")
else:
    print("Outdated Backup")
    
    
    
#18. Support Response Time
response_hrs =3
if response_hrs <=1:
    print("Immediate Support")
elif response_hrs <=4:
    print("Fast Support")
elif response_hrs <=12:
    print("Average Support")
else:
    print("Slow Support")
    
#19.  Training Completion
#25,50,75,100
progress = 75

if progress<=25:
    print("Just Started")
elif progress <=50:
    progress("Making Progress")
elif progress <=75:
    print("Almost Done")
else:
    print("Completed")
    
    
#20. Discount Offer
cart_value = 600
if cart_value >=2000:
    print("30'%' discount ")
elif cart_value >=1000:
    print("20'%' discount")
elif cart_value >=500:
    print("10'%' discount")
else:
    print("No discount")
    
    
#21. Project Status
status = 95
if status==100:
    print("Project Completed")
elif status>=75:
    print("Project almost Completed")
elif status >=50:
    print("Project Halfway Completed")
else:
    print("Not Done")
    
    
#22. RisK Level
risk_level = 40
if risk_level >=80:
    print("Critical RISK")
elif risk_level >=50:
    print("High Risk")
elif risk_level >=20:
    print("Moderate Risk")
else:
    print("Low Risk")
    
    
#23. App Rating
rating =4.2
if rating>=4.5:
    print("Excellent App")
elif rating >=4.0:
    print("Very Good App")
elif rating >=3.0:
    print("Good App")
else:
    print("Needs an Improvement")
    
    
#24. Energy Consumption
consumption_kwh = 300
if consumption_kwh <100:
    print("Low Useage")
elif consumption_kwh < 300:
    print("Moderate Useage")
elif consumption_kwh <500:
    print("High Usage")
else:
    print("Very High Usage")
    
#25. Test Execution
execution_sec = 120
if execution_sec<=30:
    print("Fast Test")
elif execution_sec <=60:
    print('Acceptable Test')
elif execution_sec <=180:
    print("Slow Test")
else:
    print("Very Slow Test")
    

#26. Database Query Time
query_ms = 250
#100,300,1000
if query_ms <100:
    print("Optimal Performance")
elif query_ms <300:
    print("Acceptable Performance")
elif query_ms < 1000:
    print("Slow Peformance")
else:
    print("Critical Performance Issues")
    
    
#27. Attendance Percentage
attendance = 65
if attendance >=90:
    print("Excellent")
elif attendance>=75:
    print("Good Attendance")
elif attendance >=50:
    print("Less Attendance")
else:
    print("Very Poor Attendance")
    
    
#28. Credit Score
score = 780
if score >=800:
    print("Excellent Credit")
elif score >=700:
    print("Good Credit")
elif score >=600:
    print("Fair Credit")
else:
    print("Poor Credit")    
    

#29. Video Resolution
resolution ='1080p'
if resolution=='4k':
    print("Ultra HD")
elif resolution=='1080p':
    print("FULL HD")
elif resolution=='720p':
    print("HD")
else:
    print("SD") 

    
#30. Employee Rating
emp_rating = 4.8
if emp_rating >=4.5:
    print("Outstanding EMPLOYEE")
elif emp_rating>=4.0:
    print("Excellent Employee")
elif emp_rating>=3.0:
    print("Good Employees")
else:
    print("Needs Improvement")
    


    
    
