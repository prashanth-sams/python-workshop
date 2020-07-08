class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def record(self):
        vault = dict(name=self.name, age=self.age)
        print(vault)


x = Person('Prashanth', 30)
x.record()