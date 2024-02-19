l=[]
n= int(input("enter number of books: "))
for i in range(n):
    bookname=(input("enter name of the book: "))
    name=input("enter author name: ")
    price=int(input("enter price of the book: "))
    year=int(input("enter year of the book: "))
    t=[bookname,name,price,year]
    l.append(t)
print(type(l))
    #bookname

"""for i in range(0,n):
    print(l[i][0])

#book details where price<200
    
for i in range(0,n):
    if(l[i][2]>200):
        print(l[i])

# find average price of all books
sum=0        
for i in range(0,n):
    sum=sum+l[i][2] 
print("average price of all book is: ",sum/n)   

#Count number of books published between 2010 and 2020.
count=0
for i in range(0,n):
    if 2010<=l[i][3]<=2020:
        count+=1
print(count)    

#Display authors names who have published more than 1 book
count_auth=0
m=[]
for i in range(0,n):
   for j in i:
     if l[1][1]==l[1][j]:
        pass"""
   








