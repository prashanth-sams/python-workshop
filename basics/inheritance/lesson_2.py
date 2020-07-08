class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def record(self):
        vault = dict(name=self.name, age=self.age)
        print(vault)


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        # Person.__init__(self, name, age)
        self.sex = 'male'


Student('Prashanth', 30).record()
Student('Sams', 31).record()
print(Student('Sams', 31).sex)
