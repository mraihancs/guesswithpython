import random

guess = int(input("Enter a number between 1 to 5 :"))
number = random.randint(1,5)
if guess == number:
    print("You have won!!! Congratulations!")

else:
    print("You have lost.. Try Again!")

print("Guessing number is: ",number)
