# Create a function that adds "." between each letter
# of a given string

def add_dots(string):
    chars = list(string)
    variable = "."
    return variable.join(chars)

def remove_dots(string):
    return string.replace(".", "")