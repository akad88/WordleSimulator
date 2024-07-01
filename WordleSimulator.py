import random
import time

# Getting the input word from the user
def userInput(numGuesses):
    userWord = input(f"{numGuesses} guesses left. Make your guess: ")
    blank = ""
    for element in range(0, len(userWord)):
        blank += userWord[element].upper()
    return blank


def numCorrectPos(wordOne, wordTwo):
    # List of indexes where the letter in the user-entered word is in the correct position
    correctPosIndex = []
    for x in range(0, len(wordOne)):
        if (wordOne[x] == wordTwo[x]):
            correctPosIndex.append(x)
    return correctPosIndex

def numWrongPos(userWord, secretWord):
    # List of indexes where the letter in the user-entered word is in the secret word but in the wrong position
    wrongPosIndex = []
    for x in range(0, len(userWord)):
        for y in range(0, len(secretWord)):
            if (x!=y):
                if (userWord[x] == secretWord[y]):
                    wrongPosIndex.append(x)
    return wrongPosIndex

#Comparing two words to see if they are the same
def comparingWords(wordOne, wordTwo):
    if (wordOne == wordTwo):
        return 1
    else:
        return 0

#Making sure the user-entered word is a 5 letter word
def checkingInput(word):
    if (len(word)!=5):
        return 0
    for i in range(0, len(word)):
        if (word[i].isalpha() == False):
            return 0
    return 1

#List of secret words user has to guess
secretWords = ["SYRUP", "FLASK", "ALIEN", "VOUCH", "FIERY", "BURNT", "MINCE", "SILKY", "MUSIC", "QUART", "SUGAR", "WHACK", "WATCH", "QUERY", "SQUAD", "LAPSE", "CAULK", "FAVOR", "HUMOR", "ULTRA", "ULCER", "VENUS", "CRAZY", "LYMPH", "LATER", "YACHT", "FLUID", "WHITE", "TABLE", "CRAFT"]

#User starts with 6 guesses
numGuesses = 6

#Randomizing secret word
secretWord = secretWords[random.randint(0, len(secretWords)-1)]

#Explaining general rules of Word Guesser Game

print("Welcome to Word Guesser! This is a game where you guess a secret five-letter word, given certain clues.\n")

print("The game will ask you for a word to enter. Your entered word must only have five letters. If it doesn't, you will be prompted again and again for a valid input.\n")

print("When you enter your word, the game will display your entered word, letter by letter.\n")

print("Symbols will pop up under each letter to help you guess the secret word.\n")

print("SYMBOLS:\n")

print("O ---> this letter is in the correct position\n")

print("/ ---> this letter is in the secret word but in the wrong position\n")

print("X ---> this letter is not in the word\n")

print("These symbols should help you guess the secret word.\n")

print("You have 6 guesses. Have fun!\n")

#Will run until the user runs out of guesses
while (numGuesses != 0):
    userWord = userInput(numGuesses)
    while(checkingInput(userWord) != 1):
        userWord = userInput(numGuesses)
    #Will break loop and display Congrats if user guesses secret word
    if (comparingWords(userWord, secretWord)==1):
        print("Good job! You guessed the word correctly!")
        break
    else:
        #Formatting the output of game
        for letter in range(0, len(userWord)):
            print(f"_{userWord[letter]}_ ", end="")
        print("")
        
        #List of symbols under corresponding indexes of user-enterred word
        #Symbols start out as all X but will change
        indices = ["X", "X", "X", "X", "X"]
        
        #Indexes of user-entered word where letter is in correct position
        #Corresponding indexes will have the symbol O under
        for x in numCorrectPos(userWord, secretWord):
            indices[x] = "O"
        
        #Indexes of user-entered word where letter is in secret word but in wrong position
        #Corresponding indexes will have the symbol / under
        for y in numWrongPos(userWord, secretWord):
            indices[y] = "/"
        
        #Printing symbols under letters
        for index in indices:
            print(f" {index}  ", end="")
        print("\n")
        
        #User will have one less guess
        numGuesses -= 1
        
        #User loses if they've run out of guesses
        if (numGuesses == 0):
            print("Sorry! You have lost!")
            print(f"The secret word was {secretWord}")
            break










