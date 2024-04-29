d={}
n=int(input("enter no of students: "))
for i in range(n):
    k=int(input("enter roll no: "))
    v=float(input("enter cgpa: "))
    d.update({k:v}) 
print(d)
s=0
avg=0
for i in d.values():
    s=s+i
    avg=s/n
print(avg)
m=max(d.values())
for i in d:
    if(d[i]==m):
        top=i
print(top)

for i,j in d.items():
    if j<5:
      d[i]=j-1
print(d)
