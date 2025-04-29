
class Dog:
    def __init__(self,breed,lifeex,price,gender,weight,height):
        self.breed = breed
        self.lifeex=lifeex
        self.price=price
        self.gender=gender
        self.weight=weight
        self.height=height

    def showFeatures(self):
        print("Breed: ",self.breed)
        print("Life expectancy in years: ",self.lifeex)
        print("Price in thousand(s): ",self.price)
        print("Gender: ",self.gender)
        print("Weight in kilos: ",self.weight)
        print("Height in cm: ",self.height)
        print()


dog1=Dog("Beagle",13.5,1.2,"Male",12,39)
dog2=Dog("Labrador",12,1,"Female",25,54)
dog3=Dog("German Shepherd",13,2,"Male",37,66)

dog1.showFeatures()
dog2.showFeatures()
dog3.showFeatures()     