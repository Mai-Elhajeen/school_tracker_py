import os
from utils.file_handler import read_file, write_file
from models.student import Student
from models.course import Course

STUDENT_FILE = os.path.join("data", "students.txt")
class Main:
    def menu(self):
        print("""
Menu:
What is your choice:
1. Show all students
2. Show all courses
3. Show students in class (should ask if ranked or not)
4. Register a new student
5. Create new class
6. Save and exit
              """)
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Invalid Input. Please enter a number.")
        return -1

    def load_students(self):
        students=[]
        lines_in_students_file = read_file(STUDENT_FILE)
        for line_student in lines_in_students_file:
            student_data = line_student.strip().split(",")
            id= student_data[0]
            name = student_data[1]
            year_of_birth = int(student_data[2])
            scores = student_data[3].split("|") if len(student_data) > 3 and student_data[3] else []
            student = Student(id, name, year_of_birth, scores)
            students.append(student)
        return students

    def get_student_by_id(self, ids_students, students):
        studs = []
        for id in ids_students:
            for student in students:
                if student.id == id:
                    studs.append(student)
                    break
        return studs

    def load_courses(self, students):
        courses=[]
        lines_in_courses_file = read_file(os.path.join("data", "courses.txt"))
        for line_course in lines_in_courses_file:
            course_data = line_course.strip().split(",")
            id= course_data[0]
            name = course_data[1]
            ids_students = course_data[2].split("|")
            studs = self.get_student_by_id(ids_students, students)
            course = Course(id, name, studs)
            courses.append(course)
        return courses
    
    def show_all_students(self, students):
        for student in students:
            student.introduce()
    
    def show_all_courses(self, courses):
        for course in courses:
            course.course_info()

    def get_course_by_id(self, id, courses):
        for course in courses:
            if course.id == id:
                return course
    
    def get_students_data_for_file(self, students):
        data = ""
        for student in students:
            scores = "|".join(student.scores)
            line = f"{student.id},{student.name},{student.year_of_birth},{scores}"
            data += line + "\n"
        return data

    def get_courses_data_for_file(self, courses):
        data=""
        for course in courses:
            ids_students = "|".join([student.id for student in course.students])
            line = f"{course.id},{course.name},{ids_students}"
            data += line + "\n"
        return data

    def register_new_student(self, students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        year_of_birth = int(input("Enter student year of birth: "))
        scores = []
        while True:
            score = input("Enter a score (or 'done' to finish): ")
            if score.lower() == "done":
                break
            scores.append(score)
        new_student = Student(id, name, year_of_birth, scores)
        students.append(new_student)

    def create_new_course(self, courses, students):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        ids_students = input("Enter student IDs for this course (separated by '|'): ").split("|")
        studs = self.get_student_by_id(ids_students, students)
        new_course = Course(id, name, studs)
        courses.append(new_course)

    def run(self):
        students = self.load_students()
        courses = self.load_courses(students)
        choice = self.menu()
        while True:
            if choice ==1:
                self.show_all_students(students)
            elif choice ==2:
                self.show_all_courses(courses)

            elif choice ==3:
                rank = input("Enter 1 to show ranked students, or 0 to show not ranked students: ")
                if rank == "1":
                    rank = True
                else:
                    rank = False
                self.show_all_courses(courses)
                course_id = input("Enter the course ID to show its students: ")
                course = self.get_course_by_id(course_id, courses)
                course.show_students(rank)
            
            elif choice ==4:
                self.register_new_student(students)

            elif choice ==5:
                self.create_new_course(courses, students)

            elif choice ==6:
                students_data  = self.get_students_data_for_file(students)
                write_file(STUDENT_FILE, students_data)

                courses_data = self.get_courses_data_for_file(courses)
                write_file(os.path.join("data", "courses.txt"), courses_data)
                print("Data saved. Exiting the program.")
                break
            choice = self.menu()
    
if __name__ == "__main__":
    main =Main()
    main.run()
