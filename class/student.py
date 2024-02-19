l=[]
n= int(input("enter number of students: "))
for i in range(n):
    rn=int(input("enter roll no: "))
    name=input("enter name: ")
    marks=int(input("enter marks: "))
    t=[rn,name,marks]
    l.append(t)
print(l)  
average=0  

# now finding average marks of each  students
for i in l:
    for j in i:
        if(j==2):
            average=(average+j[2])/n
print(average)
