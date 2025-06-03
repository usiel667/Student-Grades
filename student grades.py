#Import necessary libraries


from colorama import Fore, Style, init
# Initialize colorama

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
reset = Style.RESET_ALL

count = 0


#lists_--------------------------------------->

   
name_list =[]
class_list =[]
grade_list = []
student_id_list = []
#--------------------------------------------->

#Open student_data.txt file to read and write data
with open("student_data.txt", "r") as file:
  content = file.read()
  

#--------------------------------------------->

#ask if user wants to display existing student data or add new students
display_existing = input("Do you want to display existing student data? (yes/no): ").strip().lower()
if display_existing == 'yes':
    if content:
        print("\nExisting Student Data:")
        # Display student data in columns
        print(magenta + "Name:" + "\t" * 2 + "Student ID:\tClass:" + "\t" * 2 + "Grade:" + reset)
        for line in content.strip().splitlines():
            fields = line.split(",")
            # Ensure there are 4 fields before printing
            if len(fields) == 4:
                print(f"{fields[0]}\t{fields[1]}\t\t{fields[2]}\t\t{fields[3]}")
    else:
        print(red + "No existing student data found." + reset)


#ask user how many students to be inputed

num_students = int(input("Enter the number of students to add: "))

#collect data for each student(name, class, grade)

for i in range(num_students):
    print(f"\nstudent {i + 1}:")
    name = input("input student name:")
    student_id = input("input student ID:")
    student_class = input("input sudents class's:")
    grade = input("input student grade for class:")
   
   
   
#appened (name, class, and grade)lists
    name_list.append(name)
    student_id_list.append(student_id)
    class_list.append(student_class)
    grade_list.append(grade)
    
    #print(f"Student {i + 1} - Name: {name}, Class: {student_class}, Grade: {grade}, ID: {student_id}")
   
#combine lists into one list
student_data = [[name_list[i], student_id_list[i], class_list[i], grade_list[i]] for i in range(len(name_list))]


#print combined list
print("\nStudent Data:")

print(magenta + "Name:" + "\t" * 2 + "Student ID:\tClass:", "\t" *2 + "Grade:" + reset)
for student in student_data:
    print(f"{student[0]}\t{student[1]}\t\t{student[2]}\t\t{student[3]}")
    
    
# ask if user wants to add another student
add_another = input("\nDo you want to add another student? (yes/no): ").strip().lower()
if add_another == 'yes':
    num_students = int(input("Enter the number of additional students to add: "))
    for i in range(num_students):
        print(f"\nstudent {i + 1}:")
        name = input("input student name:")
        student_class = input("input sudents class's:")
        grade = input("input student grade for class:")
       
        # appened (name, class, and grade)lists
        name_list.append(name)
        class_list.append(student_class)
        grade_list.append(grade)
       
    # combine lists into one list
    student_data = [[name_list[i], class_list[i], grade_list[i]] for i in range(len(name_list))]
    
    # print combined list
    print("\nUpdated Student Data:")
    print("Name\tClass\tGrade")
    for student in student_data:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")


 
 
# ask if user wants to remove a student


#ask if user wants to search far a student
#  
  
    
# Search for what class a student is taking
    #Make it so the search is not case sensitive and also if you want to search for just first name or last name

search_name = input("\nEnter a student name to see their class: ")
found = False
for student in student_data:
    if student[0].lower() == search_name.lower():
            print(f"{student[0]} is taking {student[1]}")
            found = True
if not found:
        print(red + f"No class found for student named {search_name}." + reset)    #did it work



#calculate average grades of each student

#calculate average grades of each class



#