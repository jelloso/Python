#This code takes you up to the end of page 19 and adds an elif to the program.

user_reply = input ("Do you like robots? (Type yes, no, maybe or only ones with laser eyes)")  
if user_reply == "yes":
    print ("Beep boop!")
elif user_reply == "maybe":
    print ("Make up your mind, human.")
elif user_reply == "only ones with laser eyes":
    print ("Zzzap.")
elif user_reply == "no":
    print ("Well, robots don't like you either.")
else:
    print ("Your human nonsense offends us.")

