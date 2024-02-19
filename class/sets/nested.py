n=int(input("enter no. of students: "))
d={}
for i in range(n):
    roll_no=int(input("enter roll no: "))
    name=input("enter name: ")
    marks=int(input("enter marks: "))
    cgpa=float(input("enter cgpa: "))
    v=(name,marks,cgpa)
    d.update({roll_no:v})
print(d)    
for i in d: #i denotes keys
    #suppose we have to display  only roll_no,name,cgpa only
    print("roll_no:",i, "name:",d[i][0], "cgpa:",d[i][2])
