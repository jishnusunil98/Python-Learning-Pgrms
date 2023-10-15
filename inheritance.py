class Parent():
    def __init__(self,mn,p,c,t):
        self.model=mn
        self.price=p
        self.color=c
        self.type=t

    def specification(self):
        print(self.model)
        print(self.price)
        print(self.color)
        print(self.type)

class Child(Parent):
    def __init__(self,mn,p,c,t,s,m,ti):
        super(). __init__(mn,p,c,t)
        self.speed=s
        self.milage=m
        self.time=ti

    def explane(self):
        print("Its",self.model,"and",self.color,"in color and its a",self.type, "of price",self.price,".And it have a top speed of",self.speed,"km and milage of",self.milage,"kmpl and 0 to 100 in",
              self.time,"seconds")

obj=Child("Creta","20 lakhs","white","SUV",140,14,10)
obj.explane()
