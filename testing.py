
file=open('words,txt','r')
words=file.read().splitlines()
file.close()

import random 
index=random.randint(0,len(words)-1)
word=words[index]

print(word)


def lettercheckcorrect():
    
    common_letters = set(guesses) & set(word)
    incorrectguesses = set(guesses) - set(word) 
   
    if common_letters:
        1 == common_letters 
    
        return 1
        
    else:
        0 == incorrectguesses
        return 0
    
def guessesanswer():
    yesguess=[]
    tempresult= lettercheckcorrect() 
    incorrectguesses=[] 
    if tempresult == 1:
        yesguess.append(guess)
        
    if tempresult == 0:
        incorrectguesses.append(guess)
        
    return yesguess , incorrectguesses
   # return "Here are your correct guesses:" , yesguess , "Here are your incorrect guesses:" , incorrectguesses

guesses=[]
maxguesses=len(word)+3
while len(guesses) < maxguesses:
    guess=input("What letter would you like to guess? ")
    while len(guess) != 1 or guess<'a' or guess>'z':
        guess=input("What letter would you like to guess? ")   
    guesses.append(guess)
    
    
    storec=[]
    storeinc=[]
   
    storecorrect , storeincorrect = guessesanswer() 
    storec.append(storecorrect)
    storeinc.append(storeincorrect)
    print("correct ones" , storec)
    print("incorrect ones" , storeinc)
    
    
