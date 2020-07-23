class Fruit:

    """
    can modify object instance state
    can modify class state
    """
    def grapes(self):
        print('instance method')

    """
    can't modify object instance state
    can modify class state
    """
    @classmethod
    def orange(cls):
        print('class method')

    """
    can't modify object instance state
    can't modify class state
    """
    @staticmethod
    def apple():
        print('simple method')


Fruit().grapes()
Fruit().orange()
Fruit().apple()