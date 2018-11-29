tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# Full list of 'Escapes' in Python3.7
# The purpose of the \ is to encode difficult-to-type characters
# in to a string. This might mean writing height, hex values, etc.

#\\ Writes a backslash
#\' Single quote
#\" Double-quote
#\a ASCII bell (BEL) In some languages/platforms, this will make a beep. Nowadays, many don't
#\b ASCII backspace (BS) Removes previous character from string
#\f ASCII formfeed (FF) Will print next line, tabbed
#\n ASCII linefeed (LF) Will print in the next line
#\N{NAME} Prints a character desginated in unicode
#\r Carriage Return (CR) Will overwrite characters previous to this command with characters following this command
#\t ASCII tab (TAB) Indent one tab horizontally
#\v ASCII vertical tab (VT) Indent one tab vertically
#\uxxxx Prints a unicode given the 16-bit hex value xxxx
#\Uxxxxxxxx Prints a unicode given a 32-bit hex value xxxxxxxx
#\000 Print character with given octal value "000"
#\xhh Print character with given hex value "hh"
