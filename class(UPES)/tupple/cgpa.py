n=int(input("enter total number of students: "))
s=()
for i in range(n):
    name=input("enter name: ")
    cgpa=float(input("enter cgpa: "))
    s=s+((name,cgpa),)
'''for i in t:
    print("student name is: ",t(i)(0)  "cgpa is: ",t[i][1])'''
print(type(s));
      
