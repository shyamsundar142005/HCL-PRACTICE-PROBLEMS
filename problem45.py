class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.roll_no, Student.school_name)


# Creating objects
s1 = Student("Ravi", 1)
s2 = Student("Anu", 2)

print("Before changing school name:")
s1.display()
s2.display()

Student.school_name = "XYZ School"

print("\nAfter changing school name:")
s1.display()
s2.display()