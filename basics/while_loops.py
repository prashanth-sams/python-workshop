# generic
i = 0
while i < 10:
    print(i)
    i += 1

# break from 5 in 1 to 10 series
while i < 10:
    print(i)
    if i == 5: break
    i += 1

# missing 5 from 1 to 10 series
while i < 10:
    i += 1
    if i == 5: continue
    print(i)

# false condition
while i < 0:
    print(i)
else:
    print("no execution")