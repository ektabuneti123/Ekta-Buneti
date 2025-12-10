#Name - Ekta Buneti
#Roll No- F077
#Q3 E: Write a program for Hybrid inheritance
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Student Name:", self.name)


class GraduateStudent(Student):
    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree

    def show_degree(self):
        print("Degree:", self.degree)


class Certification:
    def __init__(self, course):
        self.course = course

    def show_course(self):
        print("Certified Course:", self.course)


class FinalProfile(GraduateStudent, Certification):
    def __init__(self, name, degree, course):
        GraduateStudent.__init__(self, name, degree)
        Certification.__init__(self, course)

    def show_profile(self):
        self.show_name()
        self.show_degree()
        self.show_course()


f = FinalProfile("Ekta", "B.Sc. CS", "Python Programming")
f.show_profile()
