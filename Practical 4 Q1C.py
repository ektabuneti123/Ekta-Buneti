#Name - Ekta Buneti
#Roll No- F077
#Q3 C: Write a program for Multilevel inheritance 
class Device:
    def __init__(self, brand):
        self.brand = brand

    def show_device(self):
        print("Brand:", self.brand)


class Computer(Device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor

    def show_computer(self):
        self.show_device()
        print("Processor:", self.processor)


class Laptop(Computer):
    def __init__(self, brand, processor, ram):
        super().__init__(brand, processor)
        self.ram = ram

    def show_laptop(self):
        self.show_computer()
        print("RAM:", self.ram, "GB")


l1 = Laptop("Dell", "i5", 8)
l1.show_laptop()
