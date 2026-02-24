from models.human import Human

class Student(Human):
    def __init__(self, id, name, year_of_birth, scores=[]):
        super().__init__(name, year_of_birth)
        self.id = id
        self.scores = scores if scores is not None else []
    
    def average_score(self):
        total = 0
        for score in self.scores:
            total += float(score)
        average=-1
        try:
            average = total/len(self.scores)
        except ZeroDivisionError:
            print (f"No scores available to calculate average for this student {self.id}.")
        return average

    def introduce(self):
        print(f"Hello, I am {self.name}.")
        age = 2026 - self.year_of_birth
        print(f"I am {age} years old.")
        average = self.average_score()
        print(f"My average score is {average}.")
        print("-" * 50)

    def add_score(self, score):
        self.scores.append(score)