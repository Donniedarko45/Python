rows=int(input("input enter the number of rows: "))
space=rows//2
for space in range(0,space+1):
    print(" ")
for i in range(1,rows+1):
    for j in range(i):
        print("*")   
    print("\n")    
space+=-1  
