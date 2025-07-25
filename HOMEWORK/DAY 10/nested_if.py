"""
NESTED IF ELSE

"""

#1. Data Cleaning : Check Missing Values
missing_values =False
invalid_Values = True

if missing_values:
    print("Missing values detected")
elif invalid_Values:
    print("Invalid Values Detected")
else:
    print("Data is clean")
    
    
#2. User Authentication
username='john';password='secret'
if username=='john':
    if password=='secret':
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid User")
    
    
#3. File Download
file_download = True
file_size = 200
if file_download:
    if file_size>200:
        print("Large File Download")
    else:
        print('Small File Download')
else:
    print("Download Failed")
    
    
#4. Temperature Check with Humidity
temperature = 35
humidity = 85
if temperature >30:
    if humidity >85:
        print("Hot and humid Day")
    else:
        print("Hot and dry Day")
else:
    print("Cool Day")
    

#5. Model Evaluation
model_trained = True
accuracy =0.88
if model_trained:
    if accuracy >=0.9:
        print("Excellent Model")
    else:
        print('Model needs an Improvement')
else:
    print("Model not Trained")
    
    
#6. Server Status with Load
sever_up =  True
load = 75
if sever_up:
    if load >80:
        print("Server Loaded")
    else:
        print("Server Healthy")
else:
    print("Server Down")
    
    
    
#7. Payment Gateway Check
gateway_online = False
transaction_successful = False

if gateway_online:
    if transaction_successful:
        print("Payment Processed")
    else:
        print("Payment Failed")
else:
    print("Gateway Unavailable")
    
    
#8 . Access Rights
is_employee = True
department = 'Finance'

if is_employee:
    if department=='Finance':
        print("Access to Financial Reports Granted")
    else:
        print("Access to Finance not granted")
else:
    print("Not an employee")
    
    
    
#9. Subscription Availibilty
subscription_active = True
days_remaining = 3
if subscription_active:
    if days_remaining <=5:
        print("Subscription Expiring soon")
    else:
        print("Subscription Valid")
else:
    print("Subscription Expired")
    
    
#10: Resource Usegae
cpu = 45
ram = 75

if cpu >50:
    if ram > 75:
        print("High Cpu and ram Useage")
    else:
        print("High Cpu Useage Only")
else:
    if ram > 75:
        print("High  ram Useage")
    else:
        print("System Resources Normal")
        
        

#11. API - KEY Validation
api_key ='abc123'
api_active = False

if api_key:
    if api_active:
        print('API KEY ACTIVE')
    else:
        print('API KEY INACTIVE')
else:
    print("API KEY MISSING")
    
    
#12. Product Availability
product_in_stock = True
quality =0
if product_in_stock:
    if quality >0:
        print("Product Available")
    else:
        print("Out of Stock")
else:
    print("Product Not available")
    
    
#13. Feauture Flag and beta user
feature_enabled =True
beta_user =True
if feature_enabled:
    if beta_user:
        print("Feature Available")
    else:
        print("Feature available for production")
else:
    print('Feature Not enabled')


#14. Meeting Schedule
day ='Monday'
time = 15
if day in ['Monday','Tuesday']:
    if time <12:
        print('Morning Meeting')
    else:
        print('Afternoon Meeting')
else:
    print("No Meeting Scheduled")
    
    
#15. Student Eligibility for Exam

attendance = 85
assignment_submitted =False
if attendance >=75:
    if assignment_submitted:
        print("Eligible for Exma")
    else:
        print("Submit Assignment then you are eligible for exam")
else:
    print('Not eligible due to low attendance')
    
    
#16. Delivery Status
order_placed =True
shipping =False

if order_placed:
    if shipping:
        print("Order Shipped")
    else:
        print("Processing Order")
else:
    print("Order not Placed")
    
    
# 17. Device Online and Firmware Updates
device_online = True
firmware_version = 2.0

if device_online:
    if firmware_version <=2.5:
        print("Updates are required")
    else:
        print("Not required")  
else:
    print("Device not Online")
    
    
# 18. Financial Transactions

account_balance = 1000
withdrawal_amount = 1500

if account_balance >=withdrawal_amount:
    print("Withdrawal Allowed")
else:
    if account_balance >0:
        print("Partial Withdrawal Possible")
    else:
        print("Insufficient Funds")
        
        
        
# 19. Customer Feedback
feedbacl_given =True
customer_rating = 8.0

if feedbacl_given:
    if customer_rating>=7:
        print("Customer Satisfied")
    else:
        print("Customer not Satisfied")
else:
    print("Feedback not given")
    
    
#20. Enrollment Check
course_active =True
seats_available = 0
if course_active:
    if seats_available >0:
        print("Enrollment Available")
    else:
        print('Enrollment Closed')
else:
    print("Course Inactive")
    
    
#21. Email Delivery
email_sent = True
bounced =False
if email_sent:
    if bounced:
        print("Email Failed")
    else:
        print("Email Delivered Successfully")
else:
    print("Email not sent")
    
    
#22. Time based Greeting
hour = 20
if hour <12:
    print("Good Morning")
else:
    if hour <18:
        print("Good Afternoon")
    else:
        print("Good Evening")
        
        
#23. Git Commit Status
changed_staged = True
commit_done = False

if changed_staged:
    if commit_done:
        print("Changes committed")
    else:
        print("Commit Pending")
else:
    print("No changes staged")
    
    
#24. User Registration
email_verified = True
profile_completed = False

if email_verified:
    if profile_completed:
        print("Profile Completed")
    else:
        print("Profile Pending")
else:
    print("Email not Verified")
    
    
    
#25. Cloud Service Status
service_online = False
maintainance_scheduled = True

if service_online:
    if maintainance_scheduled:
        print('Maintainence is Pending')
    else:
        print("Maintanence Scheduled")
else:
    print("Service is Offline")
    
    
#26. Weekly Sales Performance
sales_target =5000;actual_sales = 4500
if actual_sales >=sales_target:
    print("Sales Achieved")
else:
    if sales_target >= 0.8*sales_target:
        print("Near Target")
    else:
        print('Below Target')
        
#27. API RATE LIMITING
api_calls = 950;api_limit =1000

if api_calls <=api_limit:
    print("API USEAGE WITHIN LIMITS")
else:
    print("API LIMIT REACHED")
    

#28. Document Upload
document_uploaded =True;file_size =55
if document_uploaded:
    if file_size>=50:
        print('File is too Large')
    else:
        print("File Accepted")
else:
    print("Document Upload Failed")
    
    
#29. Cloud Storage Plan
plan ='basic';storage_used =90
if plan=='basic':
    if storage_used >=80:
        print("Upgrade Recommended")
    else:
        print("Storage within Limits")
else:
    print("Premium Plan Activated")
    
    
#30. Data Pipeline Run
pipeline_ready =True;error_count =0

if pipeline_ready:
    if error_count==0:
        print("Pipeline Executed Successfully")
    else:
        print("Pipeline Executed with Errors")
else:
    print("Pipeline not ready")
    