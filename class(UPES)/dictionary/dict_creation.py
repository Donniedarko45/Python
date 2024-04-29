n=int(input("give value: "))
d={}
for i in range(n):
    i_d=int(input("enter key: "))
    v=input("name: ")
    s=input("sap id")
    m=input("course")
    n=input("batch")
    c=[v,s,m,n]
    d.update({i_d:c}) # or d[k]=v
print(d)

    
