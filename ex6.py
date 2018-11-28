#set following variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#print variables "x" and "y" to create sentences
print(x)
print(y)

#print f-strings, notated with "f" in initial position.
#Using f-strings allow you to print literal strings AND variables notated in {}
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

#Empty curly braces set so for following print with formatting
joke_evaluation = "Isn't that joke so funny?! {}"

#Since we did not use the format (print (f...)) here, we used curly braces as
#a replacement field. Anything placed in {} are evaluating code, like normal.
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side"

#printing variables with "+" operator
print (w + e)
