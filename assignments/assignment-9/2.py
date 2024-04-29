"""
 Add constructor in the above class to initialize student details of n students and
implement following methods:
a) Display() student details
b) Find Marks_percentage() of each student
c) Display result() [Note: if marks in each subject >40% than Pass else Fail] 
"""
class Student:
    def __init__(self, n):
        self.students = []
        for i in range(n):
            name = input("Enter student's name: ")
            sap_id = input("Enter student's SAP ID: ")
            phy_marks = float(input("Enter marks in Physics: "))
            chem_marks = float(input("Enter marks in Chemistry: "))
            math_marks = float(input("Enter marks in Mathematics: "))
            self.students.append({'name': name, 'sap_id': sap_id, 'marks': [phy_marks, chem_marks, math_marks]})

    def display(self):
        print("\nDetails of all students:")
        for student in self.students:
            print("Name:", student['name'])
            print("SAP ID:", student['sap_id'])
            print("Marks - Physics:", student['marks'][0])
            print("Marks - Chemistry:", student['marks'][1])
            print("Marks - Mathematics:", student['marks'][2])
            print()

    def find_marks_percentage(self):
        percentages = []
        for student in self.students:
            total_marks = sum(student['marks'])
            percentage = (total_marks / 300) * 100
            percentages.append(percentage)
        return percentages

    def display_result(self):
        print("\nResults:")
        for i, student in enumerate(self.students):
            total_marks = sum(student['marks'])
            percentage = (total_marks / 300) * 100
            result = "Pass" if all(mark >= 40 for mark in student['marks']) else "Fail"
            print(f"{i + 1}. {student['name']} - {result}")

# Create a class instance with n students
n = int(input("Enter the number of students: "))
student_class = Student(n)

# Display student details
student_class.display()

# Find and display marks percentage of each student
percentages = student_class.find_marks_percentage()
print("\nMarks Percentage of each student:")
for i, percentage in enumerate(percentages):
    print(f"{i + 1}. Percentage: {percentage:.2f}%")

# Display results
student_class.display_result()
