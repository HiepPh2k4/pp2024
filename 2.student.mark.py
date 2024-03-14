class Student:
    def __init__(self, stu_id, stu_name, stu_dob):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_dob = stu_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class Marks:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_stu_inf(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            stu_id = input(f"Enter student {i+1}'s ID: ")
            stu_name = input(f"Enter student {i+1}'s name: ")
            stu_dob = input(f"Enter student {i+1}'s date of birth: ")
            self.students.append(Student(stu_id, stu_name, stu_dob))

    def input_courses(self):
        print("--------------------------------")
        num_courses = int(input("Enter the number of courses: "))
        for j in range(num_courses):
            course_id = input(f"Enter course {j+1}'s ID: ")
            course_name = input(f"Enter course {j+1}'s name: ")
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        print("--------------------------------")
        print("Enter student's marks")
        stu_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark for the student: "))

        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][stu_id] = mark

    def list_courses(self):
        print("--------------------------------")
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"Student ID: {student.stu_id}, Student Name: {student.stu_name}, DoB: {student.stu_dob}")

    def show_stu_marks(self):
        print("--------------------------------")
        course_id = input("Enter course ID to show marks: ")
        if course_id in self.marks:
            print(f"Student marks for course {course_id}:")
            for stu_id, mark in self.marks[course_id].items():
                for student in self.students:
                    if student.stu_id == stu_id:
                        student_name = student.stu_name
                        print(f"Student Name: {student_name}, Student ID: {stu_id}, Mark: {mark}")

m = Marks()
m.input_stu_inf()
m.input_courses()
m.list_courses()
m.list_students()

while True:
    print("\n1: Input marks")
    print("2: Show student marks")
    print("3: Quit")

    choice = input("Enter 1 -> 3: ")
    if choice == '1':
        m.input_marks()
    elif choice == '2':
        m.show_stu_marks()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
