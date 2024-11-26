# Parent
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def printname(self):
    print(self.first_name, self.last_name)

p1 = Person("Name","name")
p1.printname()

# Child

class Student(Person):
    def __init__(self,first_name,last_name,year):
        super().__init__(first_name,last_name)
        self.graduation_year = year

    def welcome(self):
        print(f'Welcome {self.first_name} {self.last_name} to the graduation year of {self.graduation_year}')
s1 = Student("Dhiraj","Basavaraju",2014)
s1.printname()
s1.welcome()