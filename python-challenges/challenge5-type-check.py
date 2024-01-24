# Create a function that checks two parameters and confirms
# if the parameters are BOTH integers, returning true, otherwise
# false in any other case.

def only_ints(integer1, integer2):
    check1 = isinstance(integer1, int)
    check2 = isinstance(integer2, int)
    bool_check1 = isinstance(integer1, bool)
    bool_check2 = isinstance(integer2, bool)
    if (bool_check1 or bool_check2 == True):
        return False
    elif (check1 and check2 == True):
        return True
    else:
        return False