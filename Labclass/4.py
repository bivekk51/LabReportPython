class Cat:
    def speak(self):
        return "Meowwwww!"
class Dog:
    def speak(self):
        return "Barkkkkkk!"
def make_animal_speak(animal):
    print(animal.speak())

cat=Cat()
dog=Dog()
make_animal_speak(cat)
make_animal_speak(dog)