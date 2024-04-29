"""
3. Create programs to implement different types of inheritances
"""
#single inheritance..
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")

# Creating object of Child class
obj = Child()
obj.display()  # Child class method
obj.show()     # Parent class method

# Multiple Inheritance:

class Parent1:
    def show1(self):
        print("Parent 1 class method")

class Parent2:
    def show2(self):
        print("Parent 2 class method")

class Child(Parent1, Parent2):
    def display(self):
        print("Child class method")

# Creating object of Child class
obj = Child()
obj.display()  # Child class method
obj.show1()    # Parent 1 class method
obj.show2()    # Parent 2 class method

# Multilevel Inheritance:

class Grandparent:
    def show_grandparent(self):
        print("Grandparent class method")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class method")

class Child(Parent):
    def show_child(self):
        print("Child class method")

# Creating object of Child class
obj = Child()
obj.show_child()       # Child class method
obj.show_parent()      # Parent class method
obj.show_grandparent() # Grandparent class method


#Hierarchical Inheritance:

class Parent:
    def show_parent(self):
        print("Parent class method")

class Child1(Parent):
    def show_child1(self):
        print("Child 1 class method")

class Child2(Parent):
    def show_child2(self):
        print("Child 2 class method")

# Creating objects of Child1 and Child2 classes
obj1 = Child1()
obj2 = Child2()

obj1.show_parent()  # Parent class method
obj1.show_child1() # Child 1 class method

obj2.show_parent()  # Parent class method
obj2.show_child2() # Child 2 class method
