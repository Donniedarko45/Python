#Create a tuple to store n numeric values and find average of all values

#creating a tuple..
l=[]
n=int(input("enter total number of numbers of which you want to calculate average: "))
for i in range(n):
    num = int(input("Enter the number {}: ".format(i + 1)))
    l.append(num)
sum=0    
for i in l:
    sum=sum+i
print("average is: ",sum/n)    
    