from input import input_stu_inf, input_courses
from domains.marks import Marks

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
            student_name = next((student.stu_name for student in m.students if student.stu_id == stu_id), None)
            print(f"Student ID: {stu_id}, Student Name: {student_name}, GPA: {m.marks[course_id][stu_id]:.1f}")
    elif choice == '5':
        break
    else:
        print("Invalid choice")