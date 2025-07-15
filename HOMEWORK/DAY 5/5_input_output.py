""" 
5. INPUT AND OUTPUT

"""
#1. Ask user's name
name =input("Enter your name:")

#2. print name
print(f"Hello, {name}")

#3. Ask User's age and print it
age = int(input("Enter your age: "))
print(f"Your age is {age}")

#4. Favourite color
color = input("Enter your favorite color:")
print(f"Favorite color is: {color}")

#5. Ask city and confirm
city = input("Enter your city:");print(f"You live in {city} city")

#6. Ask for feedback
feedback = input("How was your experience?");print(f"Your feedback is {feedback}")

#7. Ask for a product rating
rating =int(input("Enter your rating: 1-5 "))
if rating <=5 and rating>=0:
    print(f"Your rating is {rating}")
else:
    print("Not valid")
    
    
#8. Ask favorite prograaming language
lang = input("Enter your favorite programming language:")
print(f"Your favorite programming language is {lang}")


#13. Dream Job
job = input("What is your dream job?");print(f"Dream job is {job}")

#16. How many siblings
siblings =int(input("Enter how many siblings: "));print(f"Siblings are {siblings}")

#18. Ask country of travel
country =input("Where do you want to Travel?");print(f"I want to travel to this {country} country")

#22. Ask for lucky number
l_number =int(input("Ask for lucky number:"))
print(f"Lucky number is {l_number}")

#23. Hobbies
hobby =input('What are your hobbies? ');print(f"Your hobbies are {hobby}")

#25. What is your favorite app
app = input("Enter your favorite app:"); print(f"Your favorite app is {app}")

