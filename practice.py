class Car:
    def __init__(self,height,width,color,priceink):
        self.height=height
        self.width=width
        self.color=color
        self.priceink=priceink

    def showFacts(self):
        print("Here are the details:")
        print("Height in inches: ",self.height)
        print("Width in inches: ",self.width)
        print("Color: ",self.color)
        print("Price in thousands: ",self.priceink)
        #for space between car 2 and car3
        print()

car1=Car(80,120,"black",13)
car2=Car(100,150,"grey",17)
car3=Car(85,700,"white",70)
#Calling Function
car1.showFacts()
car2.showFacts()
car3.showFacts()



