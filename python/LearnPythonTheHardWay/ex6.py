# This is where you declare variables,here you say there are 10 types of people. 10 in an integer.
types_of_people = 10

# Here you use the variable above as part of a string.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# an example of where a string is inside a string. The two variables above are strings.
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# another example of where a string is inside a string. In this case, it is nested twice.
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# The two strings above are concatenated.
print(w + e)