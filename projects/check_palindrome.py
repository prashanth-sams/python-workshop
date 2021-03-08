
def palindrome(value):
    
    for i in range(len(value)):
        for j in range(len(value)-i-1, -1, -1):
            if value[i] == value[j]:
                break
            else:
                return False

    return True




print(palindrome('mom'))