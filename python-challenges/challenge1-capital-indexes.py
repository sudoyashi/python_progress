# Write a function name capital_indexes. This will 
# return a list of indices that represent a capital for 
# a given string that has capital letters.

def capital_indexes(word):
    letterList = list(word)
    indexList = []
    for count, letter in enumerate(letterList):
        if letter.isupper() == False:
            pass
        else:
            indexList.append(count)
    return(indexList)