def rev(name):
    if name == "":
        return name
    else:
        return rev(name[1:]) + name[0]

print(rev('Prashanth'))