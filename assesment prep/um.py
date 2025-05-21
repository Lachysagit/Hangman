incorrectguesses=[]
maxguesses=len(word)+3

display = ("".join("_" if char != " " else " " for char in word)) 
print(display)





#Makes sure your allowed to guess again and checks if guess is valid
while len(incorrectguesses) < maxguesses:
    hangman=['\n', ' ___\n', '|   \n|   \n|   \n|   \n|   \n|\n|___', ' ___\n|   \n|   \n|   \n|   \n|\n|___\n', ' ___\n|  |\n|   \n|   \n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|   \n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|  |\n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|  |\n|  A\n|\n|___\n', ' ___\n|  |\n|  o\n|  +\n|  A\n|\n|___\n']     
    guess = ""
    while len(guess) != 1:
        guess = input("What letter would you like to guess? ").lower()    

    #replaces unguessed characters with underscores
    print("Incorrect guesses:", incorrectguesses)
    print("Correct guesses:", correctguesses)
    print(current_display)
    print(f"The word is {current_display}")
    print(hangman[len(incorrectguesses)])
    #Losing message and shows the Answer
    if len(incorrectguesses) == len(hangman) - 1:
        print(F"You have run out of guesses. HANGMAN! The word was: {word}")
        break

    


    #Win condition
    if "_" not in current_display:
        print("Congratulations! You've guessed the word correctly!")
        break


#Losing message and shows the Answer
print(F"You have run out of guesses. HANGMAN! The word was: {word}")
