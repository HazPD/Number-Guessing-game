import random
import math 
UserGuess = 0       #Declaration for UserGuess
lives = 0           #Declaration for Attempts
Num = 1             #Declaration for Num that will be randomly chosen
play = True         #Declaration for play status so that game will always be played as long as user wants to play


print("Welcome to my first project!")

#loop for highest range input

while play:

    max = int(input("What's the highest number you want for your range? "))
    Num = random.randint(1,max) #Draw random numbers from 1 to Max number
    print(Num) 
    #loop for actual guessing

    while play == True:

                UserGuess = int(input("Guess the number between 1 and " + str(max) + ": "))
                lives = lives + 1                                   #Increment on Lives for every guess

                if lives == 5:                                      #Game ends on 5 wrong guess
                    print("You ran out of lives")
                    play = False
                    break

                if UserGuess == Num:                                #Game ends upon guessing the right number.. Of course. duh? 
                    print("You guess the number!")   
                    play =  False
                    break

                elif UserGuess > Num:
                    print("Your guess is higher")
                else:
                    print("Your guess is lower")
               
                
    again = int(input("Would you like to play again? 1 for yes, 2 for no: "))  

    if again == 1:                
        play = True #executes the loop to play again
               
    elif again == 2:
        print("Thank you for playing")
        play = False 
    else:
        print("Input is invalid, exiting the game. Thank you for playing!")
        play = False 
        



