from input import input_stu_inf, input_courses
from domains.marks import Marks
from compression import compress, decompress, check
import pickle
import threading

if check():
    decompress()

class Pickle:
    def load_data(self):
        students_info = []
        courses_info = []
        marks_data = []

        with open("C:\\Users\\phamh\\pp2024\\pw8\\students.pkl", "rb") as f:
            students_info = pickle.load(f)
        with open("C:\\Users\\phamh\\pp2024\\pw8\\courses.pkl", "rb") as f:
            courses_info = pickle.load(f)
        with open("C:\\Users\\phamh\\pp2024\\pw8\\marks.pkl", "rb") as f:
            marks_data.append(pickle.load(f))
        return students_info, courses_info, marks_data

    def save_data(self, students_info, courses_info, marks_data):
        with open("C:\\Users\\phamh\\pp2024\\pw8\\students.pkl", "wb") as f:
            pickle.dump(students_info, f)
        with open("C:\\Users\\phamh\\pp2024\\pw8\\courses.pkl", "wb") as f:
            pickle.dump(courses_info, f)
        with open("C:\\Users\\phamh\\pp2024\\pw8\\marks.pkl", "wb") as f:
            for data in marks_data:
                pickle.dump(data, f)

    def bgthread_load_data(self):
        t1 = threading.Thread(target = self.load_data)
        t1.start()
        
    def bgthread_save_data(self, students_info, courses_info, marks_data):
        t2 = threading.Thread(target = self.save_data, args=(students_info, courses_info, marks_data))
        t2.start()

p = Pickle()
p.bgthread_load_data()

m = Marks()
input_stu_inf(m)
input_courses(m)
m.list_courses()
m.list_students()

while True:
    print("\n1: Input marks")
    print("2: Show student marks")
    print("3: Calculate GPA")
    print("4: Sort GPA")
    print("5: Save data")
    print("6: Compress")
    print("7: End")


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
            student_name = next((student.stu_name for student in m.students if student.stu_id == stu_id), None)
            print(f"Student ID: {stu_id}, Student Name: {student_name}, GPA: {m.marks[course_id][stu_id]:.1f}")
    elif choice == '5':
        p.bgthread_save_data(m.students, m.courses, m.marks)
        print("Saved successfully")
    elif choice == '6':
        compress()   
        print("Compressed successfully")
    elif choice == '7':
        break
    else:
        print("Invalid choice")
        