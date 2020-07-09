class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def record(self):
        vault = dict(name=self.name, age=self.age)
        print(vault)


class Student(Person):

    def __init__(self, n, a):
        super().__init__(n, a)

    def welcome(self):
        print(f"{self.name} {self.age}")


Student('Sams', 31).welcome()
