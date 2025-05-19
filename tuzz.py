file=open('words.txt','r')
words=file.read().splitlines()
file.close()

import random 
index=random.randint(0,len(words)-1)
word=words[index]
    
    


guesses=[]
correctguesses=set()
incorrectguesses=[]
maxguesses=len(word)+3
print(word)
display = ("".join("_" if char != " " else " " for char in word)) 
print(display)

while len(incorrectguesses) < maxguesses:
    guess = ""
    while len(guess) != 1:
        guess=input("What letter would you like to guess? ").lower()    
    if not guess.isalpha():
        print("Invalid guess, no numbers accepted, try again")
        continue
    if guess in incorrectguesses:
        print(f"You have already guessed {guess} try again")
        continue
    if guess in correctguesses:
        print(f"You have already guessed {guess} try again")
        continue
    if  "_" not in display:
        print("done")
    
    
    guesses.append(guess)
    
    if guess in word:
        correctguesses.add(guess)
        print("Incorrect guesses" , incorrectguesses)
        print("Correct guesses" , correctguesses)
        print ("".join(letter if letter == " " or letter in correctguesses else "_" for letter in word))
            
        
    else:
        if guess not in incorrectguesses:
            incorrectguesses.append(guess)
        print("Incorrect guesses" , incorrectguesses)
        print("Correct guesses" , correctguesses)
        print ("".join(letter if letter == " " or letter in correctguesses else "_" for letter in word))
        

print("You have ran out of guesses, HANGMAN")
   
        