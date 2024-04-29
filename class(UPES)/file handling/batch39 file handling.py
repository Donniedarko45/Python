def read_file(filename):
#read File
    fobj=open(filename,"r")
    cont=fobj.read()
    fobj.close()
    return cont
    



def file_append(filename,val):
    fobj=open(filename,"a")   
    fobj.write(name+"\n")
    fobj.close()


def create_file(filename):
    fobj=open(filename,"w")
    fobj.close()



def add(filename):
    s=0
    with open(filename,"r") as fobj:
        for i in fobj:
            s=s+int(i)
    return s



while(True):
    print("0.Create file 1.Read file 2.Append Data 3. Add numbers4. Exit")
    ch=int(input("Enter Choice:"))
    
    if ch==0:
        create_file("file.txt")

    elif ch==1: 
        print(read_file("file.txt"))
    elif ch==2:
        name=input("Enter number:")
        file_append("file.txt",name)
    elif ch==3:
        print("Total=",add("file.txt"))
    elif ch==4:
        break
        
