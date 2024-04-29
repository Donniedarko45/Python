a=input("enter a string: ")
b=input("enter a substring: ")
count=0
for i in range(len(a)):
    if(a[i:i+len(b)]==b):
        count+=1
print(count)    
    