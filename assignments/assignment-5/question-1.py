temp=input("enter the string: ")
count=0
for i in temp:
    if(ord(i)>=65 and ord(i)<97):
        count+=1
        print(i)
print("number of capital letters is: {}".format(count))   

