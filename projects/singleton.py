class Base(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Base, cls).__new__(cls, *args, **kwargs) 
        return cls._instance

if __name__ == "__main__":
    B1 = Base()
    B2 = Base()
    print(B1)
    print(B2)