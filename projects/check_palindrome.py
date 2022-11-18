# method #1
def palindrome(value):
    
    for i in range(len(value)):
        for j in range(len(value)-i-1, -1, -1):
            if value[i] == value[j]:
                break
            else:
                return False

    return True

print(palindrome('mom'))

# method #2
def palindrome(k):
    for i in range(len(k)):
        for j in range(len(k)-i, 0, -1):
            print(j)
            if k[i]==k[j-1]:
                break
            else:
                return False
    return True

print(palindrome("mam"))