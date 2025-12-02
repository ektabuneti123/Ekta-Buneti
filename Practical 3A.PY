#Name - Ekta Buneti
#Roll no - F077
#Q3(A)Write a program to create a class constructor and methods,
#initialize object using constructor and all the methods.
class CS:
    
 def __init__(self, name):
    self.name = name

 def method(self):
     print("This a method")
     print("Hello!, My name is" + self.name)

 def study(self):
     print("We are studying OOPs in Python")

print(CS)
p1=CS("Yash")
p2=CS("Ayush")

p1.method()
p2.method()
p2.study()
