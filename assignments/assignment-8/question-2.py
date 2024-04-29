"""2. Store integers in a file.
a. Find the max number
b. Find average of all numbers
c. Count number of numbers greater than 100"""

def storing_integers(filename):
    f = open(filename, "w")
    n = int(input("Enter how many numbers do you want to add in a file: "))
    for i in range(n):
        nums = int(input('Enter a number: '))
        f.write(str(nums) +"\n")                                                                                    
    f.close()
    return filename

def count_num_greater_than_100(filename):
    f=open(filename,"r")
    count=0
    l=[]
    for nums in f:
        num=int(nums.strip())
        if(num>100):
            count+=1 
    return print("number greater than 100 is: ",count)        

def max_num(filename):
    f = open(filename)
    l = []
    #we have stored integers in form of string and for removing space we will use strip fxn...
    for nums in f:
        num = int(nums.strip())
        l.append(num)
    f.close() 
    highest_int = max(l)
    return highest_int

def average(filename):
    f=open(filename)
    sum=0
    count=0
    for nums in f:
        num = int(nums.strip())
        sum=sum+num
        count=count+1
    f.close()    
    avg=sum/count    
    return print("average is: ",avg)  


filename = "integer.txt"
storing_integers(filename)
max_number = max_num(filename)
print("Max number:", max_number)
average(filename)
count_num_greater_than_100(filename)
