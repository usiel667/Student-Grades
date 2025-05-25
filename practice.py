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
y = gradebook[2]
gradebook.remove(y)
print(gradebook)



from colorama import Fore, Style, init



red = Fore.RED
blue = Fore.BLUE
reset = Style.RESET_ALL
count = 0


#lists_--------------------------------------->

list_types = ['appened',
              'clear',
              'copy',
              'count',
            'extend',
            'extend',
            'index',
            'insert',
            'pop',
            'remove',
            'reverse',
            'sort']
flavors = ["vanilla", "chocolate", "cookie dough"]
toppings = ["hor fudge", "oreos", "marshmellows"]

catagories = ["NAME", "CLASS", "GRADE"]
list_a = [1, 2, 3, 4, 5]
list_b = [["Allen", "english", 67.5],
          ["karren", "math", 79.9],
          ["Travis", "physics", 95.5],
          ["travers", "science", 87.5],
          ["Arken", "physics", 76]
          ]
       
       
print(list_b)
sorted_list = sorted(list_b)
#list_b.sort()
print(sorted_list)
appened_a = sorted_list.append(["jenice", "english", 87])

print(sorted_list, appened_a)
sorted_list_b = sorted(sorted_list)
print("resorted: ", sorted_list_b)

removed_element = sorted_list_b.pop()
print(sorted_list_b)
print(red + "removed: " + reset, blue + str(removed_element) + reset)
print(Fore.RED + "hello" + reset)


#for loops_--------------------->

for number in list_a:
    print(number)


print(red + str(catagories) + reset)
print(" {}".format(red + str(catagories) + reset))
print(red + "-" * 30 + reset)
for student in list_b:
    print(student)
 
#ICE CREAM
for one in flavors:
    for two in toppings:
        print(one, "topped with", two)
       
for x in range(1, 11, 3):
    print(x)
   
for y in range(1, 21):
    if y == 13:
        continue
    else:
        print(y)
   
    if y == 14:
        break
       

#for loops_--------------------->

for print_list_values in list_types:
    #print(print_list_values)

    count += 1
    print(f"{red}{count}.{reset}{print_list_values}")
    

print("")    
count = 0
for print_list_values in list_types:
    #print(print_list_values)

    count += 1
    print(f"{red}{count}.{reset}{print_list_values}")

   #print(print_list_values) with a space
    for print_list_values in list_types:
        print("")
        break
