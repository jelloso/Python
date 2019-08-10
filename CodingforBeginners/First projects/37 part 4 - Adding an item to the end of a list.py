#This program uses the "append" code from step 5 of "Replacing, deleting and adding" on page 37 as well as the code from "Displaying the whole list" at the top of the page, steps 1 and 2.
#This program adds moon to the end of the spacelist and prints the whole list. 

spacelist = ["rocket", "planet", "asteroid", "alien"]
spacelist.append("moon")
for item in spacelist:
    print(item)
