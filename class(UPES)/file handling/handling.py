"""Create a list and take n subject marks. Find the sum of all marks and display average marks. 
(Marks should be in the range 0 to 100)
if average is less than 35 than raise exception to display "You Failed"""

students=[]
n=int(input("enter how many subjects do you have: "))
for i in range(n):
    marks=int(input("enter the marks of subject {}: ".format(i+1)))
    students.append(marks)
print(students)    
total=sum(students)
average=total/n
print(average)

try:
    pass
except:
    if average<35:
       print("you failed")
    