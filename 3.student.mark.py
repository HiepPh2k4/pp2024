import math
import numpy as np

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
        self.marks[course_id][stu_id] = math.floor(mark * 10) / 10  

    def list_courses(self):
        print("--------------------------------")
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

    def list_students(self):
        print("--------------------------------")
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
 
    def cal_gpa(self, course_id):       
        marks = np.array(list(self.marks[course_id].values()))
        credits = np.ones_like(marks)
        
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)
        gpa = weighted_sum / total_credits
        return gpa

    def sorted_gpa(self, course_id):
        sorted_stu = sorted(self.marks[course_id].items(), key=lambda x: self.marks[course_id][x[0]], reverse=True)
        return sorted_stu

m = Marks()
m.input_stu_inf()
m.input_courses()
m.list_courses()
m.list_students()

while True:
    print("\n1: Input marks")
    print("2: Show student marks")
    print("3: Calculate GPA")
    print("4: Sort GPA")
    print("5: Quit")

    choice = input("Enter 1 -> 5: ")
    if choice == '1':
        m.input_marks()
    elif choice == '2':
        m.show_stu_marks()
    elif choice == '3':
        print("--------------------------------")
        course_id = input("Enter course ID: ")
        gpa = m.cal_gpa(course_id)
        print(f"GPA for course {course_id}: {gpa:.1f}")
    elif choice == '4':
        print("--------------------------------")
        course_id = input("Enter course ID: ")
        sorted_stu = m.sorted_gpa(course_id)
        for stu_id, mark in sorted_stu:
            for student in m.students:
                if student.stu_id == stu_id:
                    student_name = student.stu_name
                    print(f"Student ID: {stu_id}, Student Name: {student_name}, GPA: {m.marks[course_id][stu_id]:.1f}")
    elif choice == '5':
        break
    else:
        print("Invalid choice")
