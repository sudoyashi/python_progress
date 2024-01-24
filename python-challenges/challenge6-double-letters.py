# Create a function that detects double, subsequent letters 
# in a given string.

def double_letters(string):
    previous = ''
    for letter in string:
        if letter == previous:
            return True
        previous = letter
    else:
        return False