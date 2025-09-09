sales = [1200, 1500, 1700, 800, 950, 2000, 2100, 1750, 1600, 1850, 1950, 2200, 2500, 3000]
print(sales)

"""

1. Basic Info (Data Types & Operators):
- Find the total sales in 14 days.
- Find the average daily sales.
- Find the highest and lowest sales days.

"""
print(sum(sales))
total1=0
for ele in sales:
    total1+=ele
print(f"Total of thr sales is {total1}")

average = total1/len(sales)
print(f'Average sales is {round(average,2)}')

print(f"Highest and lowest sales are {max(sales)} and {min(sales)} respectively. ")


"""
2. Loops & Control Structures:
- Count the number of days sales were above average.
- Count the number of days sales were below or equal to average.

"""

c1,c2=0,0
for ele in sales:
    if ele > average:
        c1+=1
    else:
        c2+=1

print(f"Numbers of days above average is : {c1}")
print(f"Numbers of days were below or equal to average : {c2}")

"""
3. List Operations:
- Create a new list that contains only the sales above ₹2000.
- Sort the sales list in descending order.
- Reverse the original sales list.

"""
new_list =[ ele for ele in sales if ele > 2000];print(new_list)
new_list1 = sorted(sales,reverse=True);print(new_list1)
sales.sort(reverse=True)
print(sales)


"""
4. Decision Making (If-Else):
- If the total sales are above ₹20,000, print "Good Performance".
- Else print "Needs Improvement".

"""

result = 'Good Performance' if total1 > 20000 else 'Needs Improvement';print(result)
"""
5. Bonus (Optional - for extra points):
- Accept a user input for a target sales number (e.g., ₹1800).
- Find how many days met or exceeded this target."""

user_input =int(input('Enter target sales'))
count=0
for ele in sales:
    if ele > user_input:
        count+=1

print(f"Target {user_input} met or exceeded on {count} days")
    
"""
6. Comprehensions (List, Tuple, Set, Dict):
- Use list comprehension to generate a new list of sales increased by 10%.
- Use tuple comprehension (via generator → tuple()) to store sales that are even numbers.
- Use set comprehension to find unique sales values greater than ₹1500.
- Use dictionary comprehension to map each day (1–14) with its sales.
"""

lst =[ ele +0.10*ele  for ele in sales];print(lst)
tup_comp = tuple( ele  for ele in sales  if ele %2==0);print(tup_comp)
set_comp = { ele for ele in sales if ele >1500};print(set_comp)

sales1 = [1200, 1500, 1700, 800, 950, 2000, 2100, 1750, 1600, 1850, 1950, 2200, 2500, 3000]
dict_comp = {i+1:sales1[i]    for i in range(0,14)};print(dict_comp)

"""
7. Built-in Functions:
- Use max(), min(), sum(), len() for analysis instead of manual loops.

"""
print(max(sales))
print(min(sales))
print(sum(sales))
print(len(sales))

"""

8. User-Defined Function:

Create a function analyze_sales(data) that:
Takes the sales list as input.

Returns a dictionary with:
- total sales,
- average sales,
- highest sales,
- lowest sales,
- performance status.

"""

def analysesalesdata(sales):
    total = sum(sales)
    average1 = round((total/len(sales)),2)
    highest = max(sales)
    lowest = min(sales)
    performance_status =  'Good Performance' if total > 20000 else 'Needs Improvement'
    
    return {'total':total,'Average':average1,'Highest':highest,'Lowest':lowest,'Performance Status':performance_status}

print(analysesalesdata(sales1))