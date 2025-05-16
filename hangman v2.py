
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
        mathcedletters = common_letters 
    
        return mathcedletters
        
    else:
        return incorrectguesses 
    
def guessesanswer():
    yesguess=[]
    tempresult= lettercheckcorrect() 
    incorrectguesses=[] 
    if isinstance(tempresult, set) and tempresult:  
        for letter in tempresult:
            if 'a' <= letter <= 'z':  
                yesguess.append(letter)
        
    if isinstance(tempresult, set) and tempresult:  
        for letter in tempresult:
            if 'a' <= letter <= 'z':
                incorrectguesses.append(letter)
        
    print("Matching guesses" , yesguess) 
    print("Non matching guesses" , incorrectguesses)          

guesses=[]
maxguesses=len(word)+3
while len(guesses) < maxguesses:
    guess = ""
    while len(guess) != 1 or guess<'a' or guess>'z':
        guess=input("What letter would you like to guess? ")   
    guesses.append(guess) 
    guessesanswer()

 
    



   











    