# Create a function that compares two lists by a given number
# If number exists in both lists or neither, return False
# If number exists in only one list, return True
def list_xor(number, list1 , list2):
    check1 = 0
    check2 = 0
    if number in list1:
        check1 = 1
    if number in list2:
        check2 = 1
    join = check1 + check2
    if join == 1:
        return True
    else:
        return False

# Smarter solution, use the '^' xor comparator
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True
