import numpy as np
import math

class Marks:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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
                student_name = next((student.stu_name for student in self.students if student.stu_id == stu_id), None)
                print(f"Student ID: {stu_id}, Student Name: {student_name}, Mark: {mark}")
        else:
            print(f"No marks are found for course {course_id}")

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