# Import necessary libraries


from colorama import Fore, Style, init

# Initial'rcarriga/nvim-notify''rcarriga/nvim-notify'coloramacoloramacoloramaize colorama
init()

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
reset = Style.RESET_ALL

count = 0


# lists_--------------------------------------->


name_list = []
student_id_list = []
class_list = []
grade_list = []

# --------------------------------------------->

# Open student_data.txt file to read and write data
with open("student_data.txt", "r") as file:
    content = file.read()


# --------------------------------------------->

# ask if user wants to display existing student data(add feature to take y or n input)
# or add new students
display_existing = (
    input("Do you want to display existing student data? (yes/no): ").strip().lower()
)
if display_existing in ["yes", "y"]:
    if content:
        print("\nExisting Student Data:")
        # Display student data in columns
        print(
            magenta + f"{'Name:':20}{'Student ID:':14}{'Class:':10}{'Grade:':5}" + reset
        )
        for line in content.strip().splitlines():
            fields = line.split(",")
            # Ensure there are 4 fields before printing
            if len(fields) == 4:
                print(f"{fields[0]:20}{fields[1]:14}{fields[2]:10}{fields[3]:5}")
    else:
        print(red + "No existing student data found." + reset)


# ask user how many students to be inputed

while True:
    num_students_input = input("Enter the number of students to add: ").strip()
    if num_students_input.isdigit():
        num_students = int(num_students_input)
        break
    else:
        print(red + "Please enter a valid number." + reset)

# collect data for each student(name, class, grade)

for i in range(num_students):
    print(f"\nstudent {i + 1}:")
    name = input("input student name:")
    student_id = input("input student ID:")
    student_class = input("input sudents class's:")
    grade = input("input student grade for class:")

    # appened (name, class, and grade)lists
    name_list.append(name)
    student_id_list.append(student_id)
    class_list.append(student_class)
    grade_list.append(grade)

    # print(f"Student {i + 1} - Name: {name}, Class: {student_class}, Grade: {grade}, ID: {student_id}")

# combine lists into one list
student_data = [
    [name_list[i], student_id_list[i], class_list[i], grade_list[i]]
    for i in range(len(name_list))
]


# print combined list
print("\nStudent Data:")

print(magenta + "Name:" + "\t" * 2 + "Student ID:\tClass:", "\t" * 2 + "Grade:" + reset)
for student in student_data:
    print(f"{student[0]}\t{student[1]}\t\t{student[2]}\t\t{student[3]}")


# ask if user wants to add another student
add_another = input("\nDo you want to add another student? (yes/no): ").strip().lower()
if add_another == "yes":
    num_students = int(input("Enter the number of additional students to add: "))
    for i in range(num_students):
        print(f"\nstudent {i + 1}:")
        name = input("input student name:")
        student_id = input("input student ID:")
        student_class = input("input sudents class's:")
        grade = input("input student grade for class:")

        # appened (name, class, and grade)lists
        name_list.append(name)
        student_id_list.append(student_id)
        class_list.append(student_class)
        grade_list.append(grade)

    # combine lists into one list
    student_data = [
        [name_list[i], student_id_list[i], class_list[i], grade_list[i]]
        for i in range(len(name_list))
    ]

    # print combined list
    print("\nUpdated Student Data:")
    print("Name\tStudent ID\tClass\tGrade")
    for student in student_data:
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}")

        # After collecting new student data and updating the lists, append the new students to student_data.txt
with open("student_data.txt", "a") as file:
    # Only write the newly added students (the last num_students in the lists)
    for i in range(len(name_list) - num_students, len(name_list)):
        file.write(
            f"{name_list[i]},{student_id_list[i]},{class_list[i]},{grade_list[i]}\n"
        )


# ask if user wants to remove a student


# ask if user wants to search far a student
#


# Search for what class a student is taking
# Make it so the search is not case sensitive and also if you want to search for just first name or last name

search_name = input("Enter a student name to see their class: ").strip().lower()
found = False
for line in content.strip().splitlines():
    fields = line.split(",")
    if len(fields) >= 3 and fields[0].strip().lower() == search_name:
        print(f"{fields[0]} is taking {fields[2]}")
        found = True
if not found:
    print(red + f"No class found for student named {search_name}." + reset)

# calculate average grades of each student

# calculate average grades of each class


#

