import random

a=( "stone", "paper","scissor",)
b=random.choice(a)

c=input("Enter your choice: ")
print("Computer's choice is",b)
if c==b:
    print("The Game is Drawn")
elif (c=="stone" and b=="scissor" or c=="scissor" and b=="paper" or c=="paper" and b=="stone"):
    print("You had Won. Your choice is",c)
elif (c=="scissor" and b=="stone" or c=="paper" and b=="scissor" or c=="stone" and b=="paper"):
    print("Computer had Won.Your choice is",b)
else:
               print("Start the game")