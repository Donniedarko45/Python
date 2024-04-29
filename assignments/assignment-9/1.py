class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks - Physics:", self.marks[0])
        print("Marks - Chemistry:", self.marks[1])
        print("Marks - Mathematics:", self.marks[2])
        print()

# Function to take inputs from user
def take_input():
    name = input("Enter student's name: ")
    sap_id = input("Enter student's SAP ID: ")
    phy_marks = float(input("Enter marks in Physics: "))
    chem_marks = float(input("Enter marks in Chemistry: "))
    math_marks = float(input("Enter marks in Mathematics: "))
    return name, sap_id, [phy_marks, chem_marks, math_marks]

# Create three instances of Student class
students = []
for _ in range(3):
    name, sap_id, marks = take_input()
    student = Student(name, sap_id, marks)
    students.append(student)

# Display details of all students
print("\nDetails of all students:")
for student in students:
    student.display_details()
