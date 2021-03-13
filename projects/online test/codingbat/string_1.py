# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
    if (str[:3] == 'not') and len(str) < 4:
        return str
    elif 'not ' in str[:4]:
        return str
    else:
        return 'not '+ str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))