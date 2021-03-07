
k = 'Prashanth'
val = []

def isVowel(i):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if i in vowel:
        return True
    else:
        return False

for i in k:
    if isVowel(i) is True:
        pass
    else:
        val.append(i)

print(val)