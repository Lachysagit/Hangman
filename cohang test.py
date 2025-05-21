
file=open('words.txt','r')
words=file.read().splitlines()
file.close()

import random 
index=random.randint(0,len(words)-1)
word=words[index]
    
    



correctguesses=set()
incorrectguesses=[]
maxguesses=len(word)+3






#Makes sure your allowed to guess again and checks if guess is valid
while len(incorrectguesses) < maxguesses:
    hangman=['\n', ' ___\n', '|   \n|   \n|   \n|   \n|   \n|\n|___', ' ___\n|   \n|   \n|   \n|   \n|\n|___\n', ' ___\n|  |\n|   \n|   \n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|   \n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|  |\n|   \n|\n|___\n', ' ___\n|  |\n|  O\n|  |\n|  A\n|\n|___\n', ' ___\n|  |\n|  o\n|  +\n|  A\n|\n|___\n']     
    guess = ""
    while len(guess) != 1:
        guess = input("What letter would you like to guess? ").lower()    
    
    if not guess.isalpha():
        print("Invalid guess, no numbers accepted, try again")
        continue
    if guess in incorrectguesses or guess in correctguesses:
        print(f"You have already guessed {guess} try again")
        continue

    

    #Checks if guess is in word
    if guess in word:
        correctguesses.add(guess)
    else:
        incorrectguesses.append(guess)

    #Display hangman progress
    current_display = "".join(letter if letter == " " or letter in correctguesses else "_" for letter in word) 
    #replaces unguessed characters with underscores
    print("Incorrect guesses:", incorrectguesses)
    print("Correct guesses:", correctguesses)
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
        
        

