# returns true
print(bool('Prashanth'))
print(bool(38))

# returns false
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool())
print(bool(()))
print(bool({}))
print(bool([]))

# return length as boolean - True
class TrueClass:
    def __len__(self):
        return 10

print(len(TrueClass()))
print(bool(TrueClass()))
print(bool(len(TrueClass())))

# return length as boolean - False
class FalseClass:
    def __len__(self):
        return 0

print(len(FalseClass()))
print(bool(FalseClass()))
print(bool(len(FalseClass())))

# return with boolean case
def value():
    return True

if value():
    print('YES')
else:
    print('NO')

# return boolean on datatype validation
print(isinstance(20, int))
print(isinstance('sams', str))