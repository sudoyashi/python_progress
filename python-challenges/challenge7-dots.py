# Create a function that adds "." between each letter
# of a given string

def add_dots(string):
    string_new = []
    for index, character in enumerate(string, len(string)):
        if index >= len(string):
            string_new += character + '.'
            print("The string length is ", len(string), ".")
            print ("The current index is ",index, ".")
    return string_new

def remove_dots(string):




string_new = []
for character in string[1:]:
    string_new += '.' + character
    return string_new






    string_char = []
    
    list1 = list(string)
    if "." in string:
        print("This string already contains a \".\", do not process.")
    else:
        for index, letter in enumerate(len(list1)-1):
            string_char.append(letter)
            string_char.append(".")
            combine = string_char.join

        return string_char