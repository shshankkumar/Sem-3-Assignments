class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Student("Rahul", 101, 78)

s1.display()
s1.result()

'''  output 
Name: Rahul
Roll No: 101
Marks: 78
Result: Pass  '''