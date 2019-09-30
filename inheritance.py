class SuperPerson:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, I'm {}" .format(self.name))


john = SuperPerson("John Smith")
john.talk()

nico = SuperPerson("Nico Jones")
nico.talk()


class NormalPerson(SuperPerson):
    def age(self):
        print("I'm {} years old")

