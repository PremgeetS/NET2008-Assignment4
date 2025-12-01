# Assignment 4 - sing2704
#number guessing game

import random
print("\n\n**********Lets play this game of number guessing!!**********\n\n")
user_input = 0
random_number = random.randint(0,100)
#print("user input = ", user_input , "Computer number = ", random_number)
while (user_input!=random_number):
    user_input = int(input("Enter a number: "))
    print(f"You enetered {user_input}")
    
    if(user_input==random_number):
        print("Yay!! You finally guessed it")
        break
    elif(user_input<random_number):
        print("You went a bit below. Try a greater number")
    elif(user_input>random_number):
        print("You went a bit above. Try a smaller number")

    