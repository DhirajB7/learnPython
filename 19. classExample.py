class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name's {self.name} & age is  {self.age}"

    def talk(self):
        return f'{self.name} says blah blah blah'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self,age):
        self.age = age




p1 = Person("Dhiraj",36)

print(p1.__str__())
print(p1.talk())

p1.set_age(35)
p1.set_name("Dhiraj B")

print(p1.get_age(),p1.get_name())

print(p1.__str__())