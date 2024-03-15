from domains.student import Student
from domains.course import Course

def input_stu_inf(self):
    num_students = int(input("Enter the number of students: "))
    students_info = []
    for i in range(num_students):
        stu_id = input(f"Enter student {i+1}'s ID: ")
        stu_name = input(f"Enter student {i+1}'s name: ")
        stu_dob = input(f"Enter student {i+1}'s date of birth: ")
        students_info.append((stu_id, stu_name, stu_dob))
        self.students.append(Student(stu_id, stu_name, stu_dob))  
            
def input_courses(self):
    print("--------------------------------")
    num_courses = int(input("Enter the number of courses: "))
    courses_info = []
    for j in range(num_courses):
        course_id = input(f"Enter course {j+1}'s ID: ")
        course_name = input(f"Enter course {j+1}'s name: ")
        courses_info.append((course_id, course_name))
        self.courses.append(Course(course_id, course_name))
