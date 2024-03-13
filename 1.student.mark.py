# student mark management
students = []
courses = []
marks = {}

def input_stu_inf():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        stu_id = input(f"Enter student {i+1}'s ID: ")
        stu_name = input(f"Enter student {i+1}'s name: ")
        stu_dob = input(f"Enter student {i+1}'s date of birth: ")
        students.append((stu_id, stu_name, stu_dob))

def input_courses():
    print("--------------------------------")
    num_courses = int(input("Enter the number of courses: "))
    for j in range(num_courses):
        course_id = input(f"Enter course {j+1}'s ID: ")
        course_name = input(f"Enter course {j+1}'s name: ")
        courses.append((course_id, course_name))

def input_marks():
    print("--------------------------------")
    print("Enter student's marks")
    stu_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    mark = float(input("Enter mark for the student: "))
    
    if course_id not in marks:
        marks[course_id] = {}
    marks[course_id][stu_id] = mark

def list_courses():
    print("--------------------------------")    
    print("List of courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}")

def list_stu():
    print("List of students:")
    for student in students:
        print(f"Student ID: {student[0]}, Student Name: {student[1]}, DoB: {student[2]}")

def show_stu_marks():
    print("--------------------------------")
    course_id = input("Enter course ID to show marks: ")
    if course_id in marks:
        print(f"Student marks for course {course_id}:")
        for stu_id, mark in marks[course_id].items():
            student_name = next((student[1] for student in students if student[0] == stu_id), None)
            print(f"Student Name: {student_name}, Student ID: {stu_id}, Mark: {mark}")
    else:
        print(f"No marks are found for course {course_id}")

input_stu_inf()
input_courses()
list_courses()
list_stu()

while True:
    print("\n1: Input marks")
    print("2: Show student marks")
    print("3: Quit")
    
    choice = input("Enter 1 -> 3: ")
    if choice == '1':
        input_marks()
    elif choice == '2':
        show_stu_marks()
    elif choice == '3':
        break
    else:
        print("Invalid choice")