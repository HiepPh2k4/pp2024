from domains.student import Student
from domains.course import Course

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
        