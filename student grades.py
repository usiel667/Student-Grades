from colorama import Fore, Style, init
# Initialize colorama

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
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


catagories = ["NAME", "CLASS", "GRADE"]


list_b = [["Allen", "english", 67.5],
          ["karren", "math", 79.9],
          ["Travis", "physics", 95.5],
          ["travers", "science", 87.5],
          ["Arken", "physics", 76]
          ]
       
       

   
print(list_b)   
   
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
    
    
# ask if user wants to add another student
 
 
# ask if user wants to remove a student

#     
  
    
    # Search for what class a student is taking
search_name = input("\nEnter a student name to see their class: ")
found = False
for student in student_data:
    if student[0].lower() == search_name.lower():
            print(f"{student[0]} is taking {student[1]}")
            found = True
if not found:
        print(f"No class found for student named {search_name}.")    #did it work



#calculate average grades of each student

#calculate average grades of each class



#