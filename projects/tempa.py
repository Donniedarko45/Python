class Subjects:
  def __init__(self):
    print("method invoked")
    self.maths_marks=int(input("Enter marks: "))
    self.phy_marks=int(input("enter marks of physics: "))

  def display(self):
    print("marks of maths:",self.maths_marks)
    print("marks of physics:",self.phy_marks) 
st1=Subjects()
st1.display()    