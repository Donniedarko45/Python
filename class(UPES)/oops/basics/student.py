def main():   
    student=get_student()
    if student[0]=="heelo":
        student[1]="some"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name=input("Name: ")
    house=input("House: ")
    return [name,house] # returning list 

if __name__=="__main__":
    main()  

# in list we can change the value 

# immutable=>you cant change values

