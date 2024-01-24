# Create a function that will return the median character
# of a given string. If a function does not have a median, 
# do not print anything.

def mid(string):
    if len(string) % 2 == 0:
        return("")
    else:
        median = int(len(string) // 2)
        return string[median: median + 1]