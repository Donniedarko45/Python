def max(filename):
  max=0
  with open(filename,"r") as fobj:
    for i in fobj:
      if max<int(i):
        max=int(i)
  return max

def read_file(filename):
#read File
    fobj=open(filename,"r")
    cont=fobj.read()
    fobj.close()
    return cont
    

def file_append(filename,val):
    fobj=open(filename,"a")   
    fobj.write(val+"\n")
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
    print("0.Create file 1.Read file 2.Append Data 3. Add numbers 4.max 5. Exit")
    ch=int(input("Enter Choice:"))
    
    if ch==0:
        create_file("fname")

    elif ch==1: 
        print(read_file("fname"))
        
    elif ch==2:
        name=input("Enter number: ")
        sapid=input("Enter sapid: ")
        cgpa=input("enter cgpa: ")
        val=name+","+sapid+","+cgpa
        file_append("fname",val)
        
    elif ch==3:
        print("Total=",add("fname"))
        
    elif ch==4:
      print(max("fname"))
        
    elif ch==5:
      break