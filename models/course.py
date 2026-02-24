class Course:
    def __init__(self, id, name, students=None):
        self.id = id
        self.name = name
        self.students = students if students is not None else []
    
    def __print_not_ranked(self):
        for student in self.students:
            student.introduce()

    def __print_ranked(self):
        for i in range(len(self.students)):
            for j in range(i, len(self.students)): 
                if self.students[i].average_score() < self.students[j].average_score():
                    stud = self.students[i]
                    self.students[i] = self.students[j]
                    self.students[j] = stud
        self.__print_not_ranked()

    def show_students(self, ranked=False):
        if not ranked:
            self.__print_not_ranked()
        else:
            self.__print_ranked()
    
    def course_info(self):
        print(f"Course ID: {self.id}, Course Name: {self.name}")
        print("-" * 30)
