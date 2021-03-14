# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):

    if not weekday or vacation:
        return True
    else:
        return False


sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)
sleep_in(True, True)