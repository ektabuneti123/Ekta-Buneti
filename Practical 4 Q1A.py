#Name - Ekta Buneti
#Roll No- F077
#Q1 A: Write a Program to demonstrate single inheritance 
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_student(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)

class Marks(Student):
    def __init__(self, name, roll, subject, marks):
        super().__init__(name, roll)
        self.subject = subject
        self.marks = marks

    def show_marks(self):
        self.show_student()
        print("Subject:", self.subject)
        print("Marks:", self.marks)


m1 = Marks("Ekta", 101, "Python", 88)
m1.show_marks()
