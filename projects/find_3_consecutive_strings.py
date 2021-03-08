def find_consecutive_3_strings(value):
    cons = 1
    result = []

    for i in range(len(value)):
        for j in range(i, len(value)-1):
            if value[i] == value[j+1]:
                cons += 1
                if cons == 3:
                    result.append(value[i])
                    break
            else:
                break
                
        cons = 1
    
    return result

print(find_consecutive_3_strings('aaxxxdddxyyzzz'))