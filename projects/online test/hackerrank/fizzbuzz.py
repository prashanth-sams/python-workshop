#!/bin/python3

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    k = 'fizzBuzz'

    for i in range(n+1):
        if i == 0:
            continue
        elif i % 15 == 0:
            print(k[:int(len(k)/2)].capitalize() + k[int(len(k)/2):].capitalize())
        elif i % 5 == 0:
            print(k[int(len(k)/2):])
        elif i % 3 == 0:
            print(k[:int(len(k)/2)].capitalize())
        
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)