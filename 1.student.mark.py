# Student mark management
students = []
courses = []
marks = {}

class Student:
    def __init__(self, stu_id, stu_name, stu_dob):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_dob = stu_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

def input_stu_inf():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        stu_id = input(f"Enter student {i+1}'s ID: ")
        stu_name = input(f"Enter student {i+1}'s name: ")
        stu_dob = input(f"Enter student {i+1}'s date of birth: ")
        students.append(Student(stu_id, stu_name, stu_dob))

def input_courses():
    print("--------------------------------")
    num_courses = int(input("Enter the number of courses: "))
    for j in range(num_courses):
        course_id = input(f"Enter course {j+1}'s ID: ")
        course_name = input(f"Enter course {j+1}'s name: ")
        courses.append(Course(course_id, course_name))

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
        print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

def list_stu():
    print("List of students:")
    for student in students:
        print(f"Student ID: {student.stu_id}, Student Name: {student.stu_name}, DoB: {student.stu_dob}")

def show_stu_marks():
    print("--------------------------------")
    course_id = input("Enter course ID to show marks: ")
    if course_id in marks:
        print(f"Student marks for course {course_id}:")
        for stu_id, mark in marks[course_id].items():
            student = next((student for student in students if student.stu_id == stu_id), None)
            print(f"Student Name: {student.stu_name}, Student ID: {stu_id}, Mark: {mark}")
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
