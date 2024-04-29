class Student:
    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa

def read_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            roll_no, name, cgpa = line.strip().split(',')
            student = Student(roll_no, name, float(cgpa))
            students.append(student)
    return students

def update_student(students, roll_no, new_name, new_cgpa):
    for student in students:
        if student.roll_no == roll_no:
            student.name = new_name
            student.cgpa = new_cgpa
            break

def save_data(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student.roll_no},{student.name},{student.cgpa}\n")

filename = 'hello.txt'

students = read_data(filename)
new_student = Student('500121084', 'Kartikey Pandey', 8.5)
students.append(new_student)
update_student(students, '500121043', 'vansh', 8.7)
save_data(students, 'updated_student_data.txt')
