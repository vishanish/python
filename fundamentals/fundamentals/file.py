num1 = 42 #variable declaration

num2 = 2.3 #variable declaration

boolean = True #Boolean

string = 'Hello World' #creates a variable with a string of 'Hello World'
“””
Data Types
Primitive
Strings
“””

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Creates a list 'pizza toppings'
“””
Data Types
Composite
List
Initialize
“””

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# Creates a dictionay/hash table called 'person'
“””
Data Types
Composite
Dictionary
Initialize
“””

fruit = ('blueberry', 'strawberry', 'banana')# Creates a tuple called 'fruit'
“””
Data Types
Composite
Tuple
Initialize
“””

print(type(fruit)) #TypeCheck Tuple

print(pizza_toppings[1])# outputs 'Sausage'
“””
Data Types
Composite
List
Access Value
“””

pizza_toppings.append('Mushrooms')# adds 'Mushrooms' to the end of the list
“””
Data Types
Composite
List
Add Value
“””

print(person['name'])# Outputs value of the key 'name' which is 'John'from dictionary 'person'
“””
Data Types
Composite
Dictionary
Access Value
“””

person['name'] = 'George' # Set value of the key 'name' to 'George' from dictionary 'person'
“””
Data Types
Composite
Dictionary
Change Value
“””

person['eye_color'] = 'blue' # Creates a new key 'color' with value of 'blue'at the end of the dictionary 'person'
“””
Data Types
Composite
Dictionary
Add Value
“””

print(fruit[2])# Outputs element of index 2 in 'fruits' which in this case is 'banana'
“””
Data Types
Composite
Tuple
Access Value
“””

if num1 > 45: #conditional if: checks if the value in the variable is greater than 45, if true then it outputs 'It's greater'
    print("It's greater")
else: #conditional else: if the if checks fails then it prints out 'It's lower'
    print("It's lower")
    # Output: It's lower
“””
conditional
if
else
“””

if len(string) < 5: #checks if the length of the value in variable sting is less than 5. If true, prints out "It's a short word!" 
    print("It's a short word!")
elif len(string) > 15: # if the initial check is false it then check if the length of the value in variable sting is greater than 15. If true, prints out "It's a long word!"
    print("It's a long word!")
else: #if the top checks are false it then comes to this default statement and prints out "Just right!"
    print("Just right!")
    # Output: "Just right!"
“””
conditional
if
else if
else
“””


for x in range(5): #1. Automatically initializes for loop with x as 0, 2. compares if x is less than 5, 3. prints x, 4. automatically increments x by 1,  5. repeats from step 2 until the boolean output is false
    print(x)
“””
for loop
stop
“””

for x in range(2,5):#1. Initializes for loop with x as 2, 2. compares if x is less than 5, 3. prints x, 4. automatically increments x by 1,  5. repeats from step 2 until the boolean output is false
    print(x)
“””
for loop
start
stop
“””

for x in range(2,10,3):#1. Initializes for loop with x as 2, 2. compares if x is less than 10, 3. prints x, 4. increments x by 3,  5. repeats from step 2 until the boolean output is false
    print(x)
“””
for loop
start
stop
increment
“””

x = 0
while(x < 5): #1. Initializes while loop with x=0, 2. compares x with <, 3. prints x, 4. increments x by 1, 5. repeats from step 2 until the boolean output is false
    print(x)
    x += 1
“””
start
while loop
stop
increment
“””

pizza_toppings.pop()# removes element from the end of the list which in this case is 'Mushrooms'
“””
Data Types
Composite
List
Delete Value
“””

pizza_toppings.pop(1) # removes element with the index of 1 from list which in this case is 'Sausage'
“””
Data Types
Composite
List
Delete Value
“””

print(person) # Output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
“””
Data Types
Composite
Dictionary
Log statement
“””

person.pop('eye_color') # removes element with key 'eye_color' and its value of 'blue', but outputs the value once

“””
Data Types
Composite
Dictionary
Delete Value
“””

print(person) # Output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

“””
Data Types
Composite
Dictionary
Log Statement
“””

for topping in pizza_toppings: #For loop looks through the list pizza_topping with variable topping
    if topping == 'Pepperoni': #If there is 'Pepperoni' in the list pizza_topping it will continue or go to log statement and if statement
        continue 
    print('After 1st if statement')#log statement
    if topping == 'Olives': #If there is 'Pepperoni' in the list pizza_topping it will break out of for loop
        break
    #Output will be: "After 1st if statement" 3 times
“””
For Loop
Conditional If
Continue
Log Statement
Conditional If
Break
“””

def print_hello_ten_times(): # function with no parameter
    for num in range(10): #for loop with fixed argument of 10
        print('Hello') #log statement
“””
Function
Parameter
“””

print_hello_ten_times()
# Function Calling with no argument so prints 'Hello' 10 times
“””
Function Calling
“”

def print_hello_x_times(x): # Function with x parameter
    for num in range(x): #for loop with input argumeny of x
        print('Hello') #log statement
“””
Function
Parameter
For Loop
Log Statement
“””

print_hello_x_times(4)
#Function Calling with argument 4 so prints 'Hello' 4 times
“””
Function Calling
Argument
“””

def print_hello_x_or_ten_times(x = 10): # Compares x with x = 10 Function
    for num in range(x):
        print('Hello')
    
“””
Function
Conditional
For Loop
Log Statement
“””

print_hello_x_or_ten_times()
#Function Calling sees if there is a value set for x or not and with no arguments so prints 'Hello' 10 times

print_hello_x_or_ten_times(4)
#Function Calling sees if there is a value set for x or not and with argument 4 so prints 'Hello' 4 times


"""
Bonus section
"""

# print(num3)  #NameError: name <variable name> is not defined
# num3 = 72 #variable declaration
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7])#IndexError: list index out of range
#   print(boolean) #log statement
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'
