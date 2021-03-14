def missing_char(str, n):
    # return 
    return str[:n] + str[n+1:]


print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))
