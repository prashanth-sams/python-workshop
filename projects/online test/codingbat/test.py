# method 2
def front_back(str):
    
    first_val = str[:1]
    last_val = str[int(len(str))-1:]

    m = list(str)

    m[0] = last_val
    m[len(str)-1] = first_val

    return (''.join(m))

result = front_back('Hey am okay now')
print(result)