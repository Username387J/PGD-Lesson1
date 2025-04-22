#OOPS: Object Oriented Programming Structure
class Student:
    #Properties / Attributes
    #inbult functions
    def __init__(self,name,age,grade,favColor,hobby):
        self.name=name
        self.age=age
        self.grade=grade
        self.favColor=favColor
        self.hobby=hobby

    def showDetails(self):
        print("The detais of the student are: " )
        print("Name :",self.name)
        print("Age :",self.age)
        print("Grade :",self.grade)
        print("Favorite color :",self.favColor)
        print("Hobby:",self.hobby)
        print()


#init function gets called itself when an object is created
s1=Student("Joshua",13,"8th Grade","black","Gaming")#object
s2=Student("Jason",7,"3rd Grade","teal","dancing")

s1.showDetails()
s2.showDetails()
