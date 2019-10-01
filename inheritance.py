class Mammal:
    def __init__(self, name, age, language):
        self.language = language
        self.name = name
        self.age = age

    def walk(self):
        print("I walk forward")


class Person(Mammal):
    def talk(self):
        print("Hi, I'm {} " .format(self.name) + "{} years old".format(self.age) + " and I speak {}" .format(self.language))


john = Person("John Smith", 32, "English")
john.talk()
nico = Person("Nico Jones", 23, "Spanish")
nico.talk()
nico.walk()