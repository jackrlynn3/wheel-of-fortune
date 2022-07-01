from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

roundNum = 0
dictionary = []
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""
usedIndices = []

# readDictionaryFile: reads in file saved as data/dictionary.txt and saves it as
#   as a list of formatted strings in the dictionary global variable
def readDictionaryFile():

    # Get global dictionary variable
    global dictionary

    # Open file
    f = open(dictionaryloc, 'r')

    # Make sure each line is properly formatted
    words = f.readlines()
    for i in range(len(words)):
        words[i] = str(words[i]).strip().lower()

    # Set dictionary to words list
    dictionary = words 

# readTurnTxtFile: reads in file saved as data/turntext.txt as string and saves
#   it under turntext global variable
def readTurnTxtFile():

    # Load in global turntext variable
    global turntext   

    # Load in corresponding text file (data/turntext.txt)
    f = open('data/turntext.txt', 'r')

    # Save string as turntext variable
    turntext = f.read()

        
def readFinalRoundTxtFile():
    global finalroundtext   
    #read in turn intial turn status "message" from file

def readRoundStatusTxtFile():
    global roundstatus
    # read the round status  the Config roundstatusloc file location 

def readWheelTxtFile():
    global wheellist
    # read the Wheel name from input using the Config wheelloc file location 

# getPlayerInfo: command line prompt will inquiry repetitiously until three valid, unique names are entered
def getPlayerInfo():
    global players
    
    # Prompt players to give their names
    print("<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n")
    print("We are now going to meet our constestants!\n")

    # Keep going until all three players names are received
    # Rules are very loose, only no repeat names and no blanks
    all_names_filled = False
    i = 0
    players_temp = [] # Makes easier to see if name is already taken
    while (not all_names_filled):

        # Get player's name
        print(f'Player {i + 1}, please enter your name!')
        name = input(f'  Player {i + 1}\'s name: ')

        # If name has already been used show message
        if (name in players_temp):
            print(f'  "{name}" has already been taken. Please enter a different name!')
        elif (name.strip() == ''):
            print('  Please enter a name with at least one character!')
        else:
            print(f'  Welcome, {name}!')
            players[i]['name'] = name
            players_temp.append(name)
            i += 1

            # Check to see if all players are in; if so, don't prompt for more names
            if (i == 3):
                print()
                print('Looks like all the players are here!\n')
                all_names_filled = True
        print()


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 

# getWord: choose a random word that has not been used by game to be the next round
def getWord():

    # Get global variables
    global dictionary
    global usedIndices
    
    # Keep going until new word is found
    new_word_found = False
    while (not new_word_found):

        # Get a random index from the dictionary
        i = random.randint(0, len(dictionary))

        # Check to see if already used
        if (i not in usedIndices):
            new_word_found = True
    
    # Get the round word
    roundWord = dictionary[i]

    # Convert the round word into underscore version
    roundUnderscoreWord = []
    for i in range(len(roundWord)):
        roundUnderscoreWord.append('_')

    # Return word and underscored version
    return roundWord,roundUnderscoreWord

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use getWord function to retrieve the word and the underscore word (blankWord)

    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    # Get random value for wheellist
    # Check for bankrupcy, and take action.
    # Check for loose turn
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    # Use guessletter function to see if guess is in word, and return count
    # Change player round total if they guess right.     
    return stillinTurn


def guessletter(letter, playerNum): 
    global players
    global blankWord
    # parameters:  take in a letter guess and player number
    # Change position of found letter in blankWord to the letter instead of underscore 
    # return goodGuess= true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.
    
    return goodGuess, count

def buyVowel(playerNum):
    global players
    global vowels
    
    # Take in a player number
    # Ensure player has 250 for buying a vowelcost
    # Use guessLetter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let goodGuess = True
    
    return goodGuess      
        
def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    
    
def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    stillinTurn = True
    while stillinTurn:
        
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
                
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus
    initPlayer = wofRoundSetup()
    
    # Keep doing things in a round until the round is done ( word is solved)
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext
    winplayer = 0
    amount = 0
    
    # Find highest gametotal player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    # If they do, add finalprize and gametotal and print out that the player won 


def main2():
    gameSetup()    

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

def main():
    global turntext
    readTurnTxtFile()
    print(turntext)

if __name__ == "__main__":
    main()
    
    

