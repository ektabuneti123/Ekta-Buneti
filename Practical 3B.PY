#Name - Ekta Buneti
#Roll no - F077
'''Q3(B)Write a program to create a class with 2 methods,
create a object calling one of the methods and from that method
call another method which returns the value back to the calling method.
'''
class CS:
    
    def __init__(self,name):
        self.name = name

    def method1(self):
        print("Calling method 2 from 1")

        message = self.method2()
        print("Method 1 received : "+ message)

    def method2(self):
        print(" Calling method 2 " +  self.name)
        return "Hello, this is method 2," + self.name

p1 = CS("Jerry")

p1.method1()
