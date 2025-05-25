from colorama import Fore, Style, init
# Initialize colorama

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
       
for print_list_values in list_types:
    #print(print_list_values)
    count += 1
    print({count}, print_list_values)
    print("")
    break
   
count = 0
for print_list_values in list_types:
    count += 1
    print(count, print_list_values)
    print("")
   
   
   
   
name_list =[]
class_list =[]
grade_list = []


#ask user how many students to be inputed

num_students = int(input("Enter the number of students to add: "))

#collect data for each student(name, class, grade)

for i in range(num_students):
    print(f"\nstudent {i + 1}:")
    name = input("input student name:")
    student_class = input("input sudents class's:")
    grade = input("input student grade for class:")
   
   
#appened (name, class, and grade)lists
    name_list.append(name)
    class_list.append(student_class)
    grade_list.append(grade)
   
#combine lists into one list
student_data = [[name_list[i], class_list[i], grade_list[i]] for i in range(len(name_list))]


#print combined list
print("\nStudent Data:")
#for print_student_data in student data:
print("Name\tClass\tGrade")
for student in student_data:
    print(f"{student[0]}\t{student[1]}\t{student[2]}")
    
    #print(student_data)
    #did it work
#maybe not

