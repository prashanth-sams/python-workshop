class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def record(self):
        vault = dict(name=self.name, age=self.age)
        print(vault)


class Student(Person):

    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex


print(Student('Sams', 31, 'Male').sex)
Person('Prashanth', 30).record()
