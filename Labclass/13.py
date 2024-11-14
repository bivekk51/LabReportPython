class Flyer:
    def fly(self):
        print("I can fly")
class Swim:
    def swim(self):
        print("I can swim")
class Duck(Flyer,Swim):
    pass
duck1=Duck()
duck1.fly()
duck1.swim()