class Animal:
    def sound(self):
        print("AniSound")
class Dog(Animal):
    def sound(self):
        print("Bark!")
Ani_Animal=Animal()
Ani_Animal.sound()
dog=Dog()
dog.sound()