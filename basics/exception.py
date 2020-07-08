# number #1
try:
    print(x)
except Exception as e:
    print(f'throw error {e}')

# number #2
try:
    raise 'asd'
except NameError as e:
    print(f'Name error {e}')
except Exception as e:
    print(f'other error {e}')

# number #3
try:
    raise 'asd'
except NameError as e:
    print(f'Name error {e}')
except Exception as e:
    print(f'other error {e}')
finally:
    print(f'finally')

# raise an exception
try:
    raise Exception('raising an exception')
except Exception as e:
    print(f'manual exception {e}')

# raise an exception
if not False: raise Exception('raising an exception')
if not False: raise TypeError("Only integers are allowed")
