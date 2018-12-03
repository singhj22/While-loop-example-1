'''
@author Jugat Singh

'''
from random import randint

num= randint(1,11)

guess= int(input("Please enter a guess between 1 and 10: "))
count= 0 
while guess != num:
    count +=1
    if guess > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    print("Try Again")
    guess= int(input("Please enter a guess between 1 and 10: "))
    
if guess== num:
    print("You guess the number correctly.")
    count+=1
    print("You guessed in", count, "tries")
