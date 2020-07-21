# generic
print([i for i in [0,1,2,True,False] if bool(None) != bool(i)])

# filter
print(list(filter(None, [0, 1, 2, 3])))
print(list(filter(None, [0, 0, 1, 2, 3])))
print(list(filter(None, [0, 1, 2, 3, True, False])))
print(list(filter(None, [0, 1, 2, 3, True, False, "", "sams"])))