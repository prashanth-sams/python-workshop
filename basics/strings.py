# print a string
print('Jesus is coming!')

# print a string in new line
print('Jesus is coming!\nAre you ready?')

# print a string in new line x2
print("""
Jesus is coming!
Are you ready?
Yes
""")

# concatenate two strings
print('Jesus is coming!' + ' Are you ready?')

# concatenate two strings as a parameter
str1 = 'Jesus is coming!'
str2 = 'Are you ready?'
print(str1 + " " + str2)

# enter input in console
name = input()
print(str1 + "\n" + name + ", " + str2)

# fetch string value through indices
print(name[0])

# get char length
print(len('am here'))
print('am here'.__len__())

k = " Jesus is coming soon"
print('coming' in k)
print('coming' not in k)
print(k[1])
print(k[2:5])
print(k[-5:-1])
print(k.strip())
print(k.lower())
print(k.upper())
l = k.upper()
print(l.isupper())
m = k.lower()
print(m.islower())
m = k.replace('soon', 'soon.')
print(m)
print(m.split(' '))
for i in k:
    print(i)

k = 'Hey! my name is {}'
age = 30
print(k.format(age))

k = '{} is my name. I am {}'
name = 'Prashanth'
age = 30
print(k.format(name, age))

k = '{1} is my name. I am {0}'
name = 'Prashanth'
age = 30
print(k.format(age, name))

k = "Jesus is coming soon \\ \t \110\145\154\154\157 \x48\x65\x6c\x6c\x6f are you ready?\b?"
print(k)

k = 'jesus is coming soon'
print(k.capitalize())