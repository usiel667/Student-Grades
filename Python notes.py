 #im now putting in my variables since boolean opoerators:not

from colorama import Fore, Style
color_B = Fore.BLUE
color_R = Fore.RED
color_G = Fore.GREEN
answer = color_R + "answer:" + Style.RESET_ALL







# this is My first lesson in python.  

#Print the greeting "Hello world!"

print("hello world")

#Print your name in "" and ''using the print() function

print("Tom Evans")
print('Tom Evans')

#print using variables 
name = "Tom Evans"
print("Hello, my name is " + name)
print(name)

#Strings and numeric data types

#integers
integer = 5

#floats
n_float = 5.5

print(integer + n_float)

print("Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing answers to mathematical questions.")
print("Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /.")

# 2 to the 10th power, or 1024
print(2 ** 10)

#Python offers a companion to the division operator called the 
#Preview: Docs A modulo calculation returns the remainder of the division between two numbers.
#modulo
# operator. The modulo operator is indicated by % and gives the remainder of a division calculation. If the two numbers are divisible, then the result of the modulo operation will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)


print("Print out every 10th customer")

first_order_remainder = 269 % 10
print(first_order_remainder)

first_order_coupon = "no"

second_order_remainder = 270 % 10
print(second_order_remainder)

second_order_coupon = "yes"


greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

#Python offers a shorthand for updating 
#Preview: Docs Loading link description
#variables
#. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += 
#Preview: Docs Operators are used to perform various operations on variables and values.
#(plus-equals) operator


# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

#The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
#We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.

print(hike_caption)


leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
print(leaves_of_grass)

#In the above example, we assign a famous poet’s words to a variable. Even though the quote contains multiple linebreaks, the code works!

#If a multi-line string isn’t assigned a variable or used in an expression it is treated as a commen


#Boolean Expressions:

#A Boolean expression is a statement that can either be true or false. The statement must be answered by true or false only, and it must be verifiable with evidence. It cannot rely on interpretation or opinion.


#Relational Operators

#Relational operators compare two values and return True or False based on the operands. For this reason, you will sometimes hear them called 
#Preview: Docs Operators are used to perform various operations on variables and values.
#comparison operators
#.
#Logical operators are used to combine multiple Boolean expressions.
#The two relational operators we’ll cover first are equals to and not equals to.

#The equals to operator (==) returns True if both its operands are the same. Otherwise, it returns False. For example, the Boolean expression a == b will return True if the values a and b are the same. Otherwise, it will return False.

#The not equals to operator (!=) is the negation of the equals to operator. The Boolean expression a != b will return True if the values a and b are different. Otherwise, it will return Fals


#boolean variables

print (Fore.RED + "boolean variables" + Style.RESET_ALL)
my_baby_bool = ("true")
print (type(my_baby_bool))
my_baby_bool_two = True
print (type(my_baby_bool_two))

#if statements

if_statements = Fore.RED + """
If statements
---------------------------------------""" + Style.RESET_ALL
print(if_statements)

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")


#Relational Operators II

relational_operators_ii = True
paragraph = Fore.RED + """

Relational Operators II
---------------------------------------""" + Style.RESET_ALL
if relational_operators_ii == True:
  print (paragraph)

ax = 40
ay = 40

# Write the first if statement here:
if ax==ay:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")



#Boolean Operators: and

x = 20
y = 20
paragraph = Fore.RED + """

"Boolean Operators: and
---------------------------------------""" + Style.RESET_ALL
if x == 20 and y == 20:
  boolean_operators_and = True
if boolean_operators_and == True:
  print(paragraph)


statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
#lets see if the two statements are true or false

print(f"Statement one: (2 + 2 + 2 >= 6) and (-1 * -1 < 0) evaluates to {statement_one}")
print(f"Statement two: (4 * 2 <= 8) and (7 - 1 == 6) evaluates to {statement_two}")

print(statement_one)
print(statement_two)

print("statement one is: " + str(statement_one))
print("statement two is: " + str(statement_two))

if statement_one and statement_two == True:
  print("Both statements are true")
  
if statement_one and statement_two == False:
  print("Both statements are false")

if statement_one == True and statement_two == False:
  print("statement one is true and  statement two is false")

if statement_one == False and statement_two == True:
  print("statement one is false and statement two is true")





credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")


print(Fore.GREEN + "I set the designaters as Red From this point on" + Style.RESET_ALL)

#Boolean Operators: or


a_or = (20 - 1 > 3) or (-5 * 2 < -10)
b_or = (9 + 5 <= 15) or (7 != 4 + 3)
paragraph = Fore.RED + """
Boolean Operators: or 
---------------------------------------""" + Style.RESET_ALL
if a_or or b_or == True:
  print(paragraph)


print(f"statement_one = (2 - 1 > 3) or (-5 * 2 == -10")

print(f"statement_two = (9 + 5 <= 15) or (7 != 4 + 3")

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")


#Boolean Operators: not

a_not = not (4 + 5 <= 9)
b_not = not (8 * 2) != 20 - 4
paragraph = Fore.RED + """
Boolean Operators: not
---------------------------------------""" + Style.RESET_ALL

if a_not or b_not == True:
  print(paragraph)


statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

print(color_R + "coding:" + Style.RESET_ALL)
paragraph_two = color_G + """credits = 120
gpa = 1.8

Boolean Operators: not  
if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")
""" + Style.RESET_ALL
print(paragraph_two)

print (color_R + "answer:" + Style.RESET_ALL)
if not credits >= 120:
  print(color_B + "You do not have enough credits to graduate." + Style.RESET_ALL)
if not gpa >= 2.0:
  print(color_B + "Your GPA is not high enough to graduate." + Style.RESET_ALL)
if not credits >= 120 and not gpa >= 2.0:
  print(color_B + "You do not meet either requirement to graduate!" + Style.RESET_ALL)


#Else Statements
c_statement = color_R + "code:" + Style.RESET_ALL

paragraph = color_R + """
Else Statements
---------------------------------------""" + Style.RESET_ALL
print(paragraph)
print(c_statement)
code = color_G + """credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")
""" + Style.RESET_ALL
print(code)

credits = 120
gpa = 1.9

print(color_R + "answer:" + Style.RESET_ALL)
if (credits >= 120) and (gpa >= 2.0):
  print(color_B + "You meet the requirements to graduate!" + Style.RESET_ALL)
else:
  print(color_B +"You do not meet the requirements to graduate." + Style.RESET_ALL)


#Else If Statements

paragraph = color_R + """
Else If Statements:
---------------------------------------""" + Style.RESET_ALL
print(paragraph)

code = color_G + """grade = 86
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
""" + Style.RESET_ALL
print(code)

print (answer)
grade = 86
if grade >= 90:
  print(color_B + "A" + Style.RESET_ALL)
elif grade >= 80:
  print(color_B + "B" + Style.RESET_ALL)
elif grade >= 70:
  print(color_B + "C" + Style.RESET_ALL)
elif grade >= 60:
  print(color_B +"D" + Style.RESET_ALL)
else:
  print(color_B + "F" + Style.RESET_ALL)



#test review

paragraph = color_R + """
test review:
---------------------------------------""" + Style.RESET_ALL
print(paragraph)

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:


code = color_G + """

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19
#print("Your weight:", weight)

print(color_B + f"Your weight: {weight:.2f}" + Style.RESET_ALL)
"""
print(code)



if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19
#print("Your weight:", weight)

print(answer) 
print(color_B + f"Your weight: {weight:.2f}" + Style.RESET_ALL)



#magic 8 ball

paragraph = color_R + """
Magic 8 Ball:
---------------------------------------""" + Style.RESET_ALL
print(paragraph)


import random

name = "Tom"
question = color_B + "will this program work?" + Style.RESET_ALL
answer =""

random_number = random.randint(1, 11)

print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Try again"
elif random_number == 11:
  answer = "Hell NO"
elif random_number >= 12:
  answer = "Error"

#Name field
if name == "":
  print(color_R + "Question: " + Style.RESET_ALL + question)
else:
  print(name + " asks:" + question)
print(color_R + "Magic 8-Ball's answer:" + Style.RESET_ALL + answer)

print("")
#Question Field
if question == "":
  print("unable to answer.  No question Given")
else:
  print(name + ": " + question + " Magic 8-Ball's answer:" + answer)
  

print("")

#shipping calculator test

paragraph = color_R + """
Shipping Calculator:
---------------------------------------""" + Style.RESET_ALL
print(paragraph)  

paragraph = color_G + """
weight = 41.5
flat_charge = 20.00
premium_charge = 125.00

#function to calculate the cost of shipping

def calculate_cost(weight, rate, flat_charge):
    return weight * rate + flat_charge

print(f"weight: {weight:.2f}lbs.")


#this section is for Ground Shipping
print("Ground Shipping")

if weight <= 2:
  ground_shipping_cost = calculate_cost(weight, 1.50, flat_charge) 
elif weight <= 6:
  ground_shipping_cost = calculate_cost(weight, 3.00, flat_charge)
elif weight <= 10:
  ground_shipping_cost = calculate_cost(weight, 4.00, flat_charge)
else:
  ground_shipping_cost = calculate_cost(weight, 4.75, flat_charge)
print(f"cost:${ground_shipping_cost:.2f}")


#this is for stating the price of ground premium
print(f"Ground Shipping Premium:${premium_charge:.2f}")


#this section is for Drone shipping:
drone_flat_charge = 0.00

if weight <=2:
  drone_shipping_charge = calculate_cost(weight, 4.50, drone_flat_charge)
elif weight <= 6:
  drone_shipping_charge = calculate_cost(weight, 9.00, drone_flat_charge)
elif weight <= 10:
  drone_shipping_charge = calculate_cost(weight, 12.00, drone_flat_charge)
else:
  drone_shipping_charge = calculate_cost(weight, 14.25, drone_flat_charge)

print(f"Drone Shipping:${drone_shipping_charge:.2f}")

if drone_shipping_charge < premium_charge and ground_shipping_cost < drone_shipping_charge:
  print(f"cheapest Method: Ground Shipping at ${ground_shipping_cost:.2f}")
elif premium_charge < ground_shipping_cost and premium_charge < drone_shipping_charge:
  print(f"Cheapest Method: Ground shipping Premium at ${premium_charge:.2f}")
else:
  print(f"Cheapest Methos: Drone Shipping at ${drone_shipping_charge:.2f}")
  """ + Style.RESET_ALL
print(paragraph)


user_input = float(input(color_B + "Enter the weight of the package in pounds: " + Style.RESET_ALL))
package_weight = user_input
#weight = 41.5
flat_charge = 20.00
premium_charge = 125.00


#function to calculate the cost of shipping

def calculate_cost(package_weight, rate, flat_charge):
    return package_weight * rate + flat_charge

print(f"weight: {package_weight:.2f}lbs.")


#this section is for Ground Shipping
print(color_R + "Ground Shipping" + Style.RESET_ALL)

if weight <= 2:
  ground_shipping_cost = calculate_cost(package_weight, 1.50, flat_charge) 
elif package_weight <= 6:
  ground_shipping_cost = calculate_cost(package_weight, 3.00, flat_charge)
elif package_weight <= 10:
  ground_shipping_cost = calculate_cost(package_weight, 4.00, flat_charge)
else:
  ground_shipping_cost = calculate_cost(package_weight, 4.75, flat_charge)
#print(f"cost:${ground_shipping_cost:.2f}")
print(color_R + "cost: " + color_B + f"${ground_shipping_cost:.2f}" + Style.RESET_ALL)

#this is for stating the price of ground premium
#print(color_B + f"Ground Shipping Premium:${premium_charge:.2f}" + Style.RESET_ALL)
print(color_R + "Ground Shipping Premium: " + color_B + f"${premium_charge:.2f}" + Style.RESET_ALL)

#this section is for Drone shipping:
drone_flat_charge = 0.00

if package_weight <=2:
  drone_shipping_charge = calculate_cost(package_weight, 4.50, drone_flat_charge)
elif package_weight <= 6:
  drone_shipping_charge = calculate_cost(package_weight, 9.00, drone_flat_charge)
elif package_weight <= 10:
  drone_shipping_charge = calculate_cost(package_weight, 12.00, drone_flat_charge)
else:
  drone_shipping_charge = calculate_cost(package_weight, 14.25, drone_flat_charge)

#print(f"Drone Shipping:${drone_shipping_charge:.2f}")
print(color_R + "Drone Shipping: " + color_B + f"${drone_shipping_charge:.2f}" + Style.RESET_ALL)


if drone_shipping_charge < premium_charge and ground_shipping_cost < drone_shipping_charge:
  print(f"cheapest Method: Ground Shipping at ${ground_shipping_cost:.2f}")
elif premium_charge < ground_shipping_cost and premium_charge < drone_shipping_charge:
  print(f"Cheapest Method: Ground shipping Premium at ${premium_charge:.2f}")
else:
  print(f"Cheapest Methos: Drone Shipping at ${drone_shipping_charge:.2f}")


paragraph = color_R + """
List Comprehensions:
---------------------------------------""" + Style.RESET_ALL
print(paragraph)

paragraph_two = color_G + """

# Checkpoint 1
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Checkpoint 2
preferred_size = ["Small", "Large", "Medium"]

# Checkpoint 3
preferred_size.append("Medium")
print(preferred_size)

# Checkpoint 4
customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]
print(customer_data)

# Checkpoint 5
customer_data[2][2] = False

# Checkpoint 6
customer_data[1].remove(False)

# Checkpoint 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
""" + Style.RESET_ALL
print(paragraph_two)

# Checkpoint 1
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Checkpoint 2
preferred_size = ["Small", "Large", "Medium"]

# Checkpoint 3
preferred_size.append("Medium")
print(preferred_size)

# Checkpoint 4
customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]
print(customer_data)

# Checkpoint 5
customer_data[2][2] = False

# Checkpoint 6
customer_data[1].remove(False)

# Checkpoint 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

paragraph_three = color_R + """
Advanced List Comprehensions:
---------------------------------------""" + Style.RESET_ALL
print(paragraph_three)

first_names = []
preferred_size = []
subscription_status = []

# Step 2: Ask the user how many customers they want to add
num_customers = int(input("Enter the number of customers to add: "))

# Step 3: Collect input for each customer
for i in range(num_customers):
    print(f"\nCustomer {i + 1}:")
    name = input("Enter the customer's name: ")
    size = input("Enter the customer's preferred size (e.g., Small, Medium, Large): ")
    status = input("Is the customer subscribed? (True/False): ")

    # Append the inputs to the respective lists
    first_names.append(name)
    preferred_size.append(size)
    subscription_status.append(status == "True")  # Convert string to boolean

# Step 4: Combine the lists into one list
customer_data = [[first_names[i], preferred_size[i], subscription_status[i]] for i in range(len(first_names))]

# Step 5: Print the combined list
print("\nCustomer Data:")
print(customer_data)

# Step 5: Option to add more customers
while True:
    add_more = input("\nDo you want to add another customer? (yes/no): ").lower()
    if add_more == "yes":
        name = input("Enter the customer's name: ")
        size = input("Enter the customer's preferred size (e.g., Small, Medium, Large): ")
        status = input("Is the customer subscribed? (True/False): ")

        # Append the new customer data
        first_names.append(name)
        preferred_size.append(size)
        subscription_status.append(status == "True")  # Convert string to boolean

        # Update the combined list
        customer_data = [[first_names[i], preferred_size[i], subscription_status[i]] for i in range(len(first_names))]

        # Print the updated list
        print("\nUpdated Customer Data:")
        print(customer_data)
    elif add_more == "no":
        print("\nFinal Customer Data:")
        print(customer_data)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


# This is a test for the list comprehension section of the course
# The code below is a test for the list comprehension section of the course.
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
gradebook.append(["computer science", 100])
print(gradebook)
gradebook.append(["visual arts", 93])
print(gradebook)
x = gradebook[-1][-1]
gradebook.append(x + 5)

print(gradebook)
#y = gradebook[2], 85
gradebook[2].remove(85)
print(gradebook)
gradebook[2].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)


#range and len function
# The range() function creates a sequence of numbers, and the len() function returns the number of items in an object.

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)
big_range_length = len(big_range)
print(big_range_length)


#slicing lists
# Slicing a list means to take a portion of the list. You can slice a list by specifying the start and end index of the slice. The slice will include the start index but not the end index.
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 
print(beginning)
middle = suitcase[2:4]
print(middle)

# The end of the list is not included in the slice.
# The slice will include the start index but not the end index.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


#counting votes
# In this exercise, you will be counting the votes for a class president. You will be given a list of votes and you will need to count how many votes each candidate received.

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

