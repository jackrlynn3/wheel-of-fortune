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
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
    'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
roundstatus = ""
finalroundtext = ""
usedIndices = []
roundUsedLetters = []

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
    f = open(turntextloc, 'r')

    # Save string as turntext variable
    turntext = f.read()
        
def readFinalRoundTxtFile():

    # Load in finalroundtext variable
    global finalroundtext   

    # Load in corresponding text file (data/turntext.txt)
    f = open(finalRoundTextLoc, 'r')

    # Save string as global variable
    finalroundtext = f.read()

def readRoundStatusTxtFile():
    global roundstatus

    # Load in corresponding text file (data/turntext.txt)
    f = open(roundstatusloc, 'r')

    # Save string as turntext variable
    roundstatus = f.read()

def readWheelTxtFile():
    global wheellist

    # read the Wheel name from input using the Config wheelloc file location 
    f = open(wheeltextloc, 'r')
    
    # Clean contents
    wheellist = f.readlines()
    for i in range(len(wheellist)):
        wheellist[i] = wheellist[i].strip()

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

# wofRoundSetup: sets up the round be resetting round variables, getting hidden word, and setting round totals to 0
def wofRoundSetup():

    # Get global variables
    global players
    global roundWord
    global blankWord
    global roundUsedLetters

    # Set round total for each player to 0
    for i in range(len(players.keys())):
        players[i]["roundtotal"] = 0

    # Return the starting player number using random integer generator
    initPlayer = random.randint(0, len(players)-1)

    # Use getWord function to retrieve the word and the underscore word (blankWord)
    roundWord, blankWord = getWord()

    # Make sure letters used is empty
    roundUsedLetters = []

    return initPlayer

def spinWheel(playerNum):
    global wheellist
    global players
    global vowels
    global roundUsedLetters

    # Get random value for wheellist
    wheel_val = wheellist[random.randint(0, len(wheellist))]

    # If 'bankrupt', end turn immediately and zero out player's round total
    if (wheel_val == "BANKRUPT"):
        players[playerNum]['roundtotal'] = 0
        print(f'You landed on the BANKRUPT space; tough luck!')
        # Pause the line so person can digest what just happened
        input("  OK? ")
        print()
        return False

    # If 'lose a turn', end turn immediately
    if (wheel_val == "LOSE A TURN"):
        print(f'You landed on the LOSE A TURN space; tough luck!')
        # Pause the line so person can digest what just happened
        input("  OK? ")
        print()
        return False

    # Convert wheel amount to integer equivalent
    wheel_val = int(wheel_val)
    print(f'You landed on the ${wheel_val} space; guess a letter')
    print(f'  Guessed letters: {roundUsedLetters}\n')

    # Ask user for letter guess
    valid_letter = False
    choice = ''
    while (not valid_letter):
        choice = str(input('  Guess: ')).lower()
        if (len(choice) != 1):
            print('You must enter a character!')
        elif (choice in roundUsedLetters):
            print('You must guess letters that haven\'t already been guessed!')
        elif (choice in vowels):
            print('You must input a consonant and not a vowel!')
        elif (not choice.isalpha()):
            print('You must input a letter!')
        else:
            print('Good choice!')
            valid_letter = True
        print()
    
    # Use guessletter function to see if guess is in word, and return count
    stillinTurn, count = guessletter(choice)

    # Change player score
    players[playerNum]['roundtotal'] += count * wheel_val

    # Print results of guess
    if (count == 0):
        print(f'There are no {choice}\'s in: {blankWord}\n')
    elif (count == 1):
        print(f'There is 1 {choice} in: {blankWord}\n')
    else:
        print(f'There are {count} {choice}\'s in: {blankWord}\n')

    # Pause the line so person can digest what just happened
    input("  OK? ")
    print()

    # Change player round total if they guess right.     
    return stillinTurn

def guessletter(letter): 
    global players
    global blankWord
    global roundWord
    global roundUsedLetters

    # Initialize count and goodGuess variables
    count = 0
    goodGuess = False

    # Change position of found letter in blankWord to the letter instead of underscore
    for i in range(len(blankWord)):
        if (letter == roundWord[i]):
            blankWord[i] = roundWord[i]
            count += 1
            goodGuess = True

    # Add letter to used list
    if (letter != '_'):
        roundUsedLetters.append(letter)

    # Return if the letter is in the word and the count
    return goodGuess, count

def buyVowel(playerNum):
    global players
    global vowels
    
    # Get a vowel to buy
    # Convert wheel amount to integer equivalent
    print(f'You want to buy a vowel')
    print(f'  Guessed vowels: {list(set(roundUsedLetters) & set(vowels))}\n')

    # Ask user for letter guess
    valid_letter = False
    choice = ''
    while (not valid_letter):
        choice = str(input('  Guess: ')).lower()
        if (len(choice) != 1):
            print('You must enter a character!')
        elif (choice in roundUsedLetters):
            print('You must guess letters that haven\'t already been guessed!')
        elif (choice in vowels):
            print('Good choice!')
            valid_letter = True
        else:
            print('You must input a vowel!')
        print()

    # Use guessletter function to see if guess is in word, and return count
    stillinTurn, count = guessletter(choice)

    # Change player score
    players[playerNum]['roundtotal'] -= vowelcost

    # Print results of guess
    if (count == 0):
        print(f'There are no {choice.upper()}\'s in: {blankWord}\n')
    elif (count == 1):
        print(f'There is 1 {choice.upper()} in: {blankWord}\n')
    else:
        print(f'There are {count} {choice.upper()}\'s in: {blankWord}\n')

    # Pause the line so person can digest what just happened
    input("  OK? ")
    print()

    # Change player round total if they guess right.     
    return stillinTurn      
        
def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    global roundUsedLetters
    
    # Ask for input of the word and check if it is the same as wordguess
    print(f'You want to guess the word')
    print(f'  Guessed letters: {roundUsedLetters}\n')

    # Ask user for letter guess
    valid_word = False
    choice = ''
    while (not valid_word):
        choice = str(input('  Guess: ')).lower()
        if (len(choice) != len(blankWord)):
            print('You must enter a guess that is the same length as the keyword!')
        else:
            print('Good choice!')
            valid_word = True
        print()

    # If the words match, give it to the player; otherwise, return false
    if (choice.lower() == roundWord.lower()):
        for i in range(len(roundWord)):
            blankWord[i] = roundWord[i]
        print(f'Your guess of "{choice}" is correct!')
    else:
        print(f'Your guess of "{choice}" is incorrect.')

    # Pause the line so person can digest what just happened
    input("  OK? ")
    print()
    
    # Always return False because guessing the word should always end turn
    return False  
    
def wofTurn(playerNum):

    # Get global variables
    global roundWord
    global blankWord
    global turntext
    global players
    global vowels
    global consonants
    global roundUsedLetters

    # Keep going with player until their is losing condition for round
    stillinTurn = True
    while stillinTurn:

        print("PLAYER NUM: "+str(playerNum))

        # Get round status
        print(turntext.format(format_word=' '.join(blankWord), p1_name=players[0]['name'],
            p1_money=players[0]['roundtotal'], p2_name=players[1]['name'],
            p2_money=players[1]['roundtotal'], p3_name=players[2]['name'],
            p3_money=players[2]['roundtotal'], curr_player=players[playerNum]['name']))
        
        # Determine what options the user has
        can_guess_consonant = False
        can_buy_vowel = False

        # Check to see if there are any consonants to spin for
        for consonant in consonants:
            if (consonant not in roundUsedLetters):
                can_guess_consonant = True
        if (can_guess_consonant):
            print('  (S)pin the wheel')
        
         # Check to see if there are any vowels to buy
        for vowel in vowels:
            if (vowel not in roundUsedLetters):
                can_buy_vowel = True
        if (players[playerNum]['roundtotal'] < vowelcost):
            can_buy_vowel = False
        if (can_buy_vowel):
            print('  (B)uy a vowel')

        # Print solve because that is always a choice
        print('  (G)uess the word')
        print()
        
        # Get user input S for spin, B for buy a vowel, G for guess the word
        choice = input('Selection: ')
        print()
        if(choice.strip().upper() == "S" and can_guess_consonant):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B" and can_buy_vowel):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print(f'{choice} is not a valid selection!')
        print()        
    
    # Check to see if round is over; if over, return False; otherwise, return True
    roundOver = True
    for i in range(len(blankWord)):
        if (blankWord[i].lower() != roundWord[i].lower()):
            roundOver = False
    if (roundOver):
        # Give the winning player their winnings
        players[playerNum]['gametotal'] += players[playerNum]['roundtotal']
        return False
    else:
        return True  

def wofRound():

    # Get global variables
    global players
    global roundWord
    global blankWord
    global roundstatus

    # Get round set up
    i_player = wofRoundSetup()

    # Debug only: print the word
    print(f'KEYWORD: {roundWord}')
    
    # Keep the roudn going until a solution is reached
    round_going = True
    while (round_going):

        # Begin the current players turn
        round_going = wofTurn(i_player)

        # Update so the next person gets to go if round is still going
        if (round_going):
            i_player += 1
            if (i_player == len(players)):
                i_player = 0
        else:
            
            # Print status of round
            print(roundstatus.format(keyword=roundWord,
                winner=players[i_player]['name'], winnings='$'+str(players[i_player]['roundtotal']),
                p1_name=players[0]['name'], p1_money=players[0]['gametotal'],
                p2_name=players[1]['name'], p2_money=players[1]['gametotal'],
                p3_name=players[2]['name'], p3_money=players[2]['gametotal']))

            # Pause the line so person can digest what just happened
            input("  OK? ")
            print()

def wofFinalRound():

    # Get global variables
    global roundWord
    global blankWord
    global finalroundtext
    global roundUsedLetters
    winplayer = 0
    
    # Determine who is playing the final round
    for i in range(1, len(players)):
        if (players[i]['gametotal'] > players[winplayer]['gametotal']):
            winplayer = i

    # Print out instructions for that player and who the player is
    print(finalroundtext)
    print(finalroundtext.format(winner=players[winplayer]['name'], winnings='$'+str(players[winplayer]['gametotal']),
        prize_money='$'+str(finalprize)))

    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    roundWord, blankWord = getWord()
    roundUsedLetters = []
    print(f'Your keyword: {(" ".join(blankWord))}\n')

    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    given_letters = ['r', 's', 't', 'l', 'n', 'e']
    for letter in given_letters:
        guessletter(letter)
    print(f'Your updated keyword after given letters: {(" ".join(blankWord))}\n')

    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    guesses = []
    all_guesses_in = False
    while (not all_guesses_in):

        # Get the first three consonants
        if (len(guesses) < 3):
            choice = str(input('  Input a consonant: ')).lower()
            if (len(choice) != 1):
                print('You must enter a character!')
            elif (choice in roundUsedLetters):
                print('You must guess letters that haven\'t already been guessed!')
            elif (choice in vowels):
                print('You must input a consonant and not a vowel!')
            elif (not choice.isalpha()):
                print('You must input a letter!')
            else:
                guesses.append(choice)
            print()

        # Get the only vowel
        elif (len(guesses) == 3):
            choice = str(input('  Input a consonant: ')).lower()
            if (len(choice) != 1):
                print('You must enter a character!')
            elif (choice in roundUsedLetters):
                print('You must guess letters that haven\'t already been guessed!')
            elif (choice in vowels):
                guesses.append(choice)
            else:
                print('You must input a vowel!')
            print()

        # End the letter inputs
        else:
            all_guesses_in = True

    # Guess the letters
    for letter in guesses:
        guessletter(letter)

    # Print out the current blankWord
    print(f'Your updated keyword after your guesses {guesses}: {(" ".join(blankWord))}\n')

    # Get user to guess word
    print('You will now be given the opportunity to guess the word once! Good luck!')

    # Ask user for word guess
    valid_word = False
    choice = ''
    while (not valid_word):
        choice = str(input('  Guess: ')).lower()
        if (len(choice) != len(blankWord)):
            print('You must enter a guess that is the same length as the keyword!')
        else:
            print('Good choice!')
            valid_word = True
        print()

    # If the words match, give it to the player; otherwise, return false
    if (choice.lower() == roundWord.lower()):
        for i in range(len(roundWord)):
            blankWord[i] = roundWord[i]
        print(f'Your guess of "{choice}" is correct! Good job!\n')
        players[winplayer]['gametotal'] += finalprize # Add in prize money
    else:
        print(f'Your guess of "{choice}" is incorrect. Better luck next time!\n')

    # Print the winner and prize money
    print(f'{players[winplayer]["name"]}, you have won this game, with total winnings of ${players[winplayer]["gametotal"]}!\n')

    # Pause the line so person can digest what just happened
    input("  OK? ")
    print()

    # Print leaving message
    print('See you again next time during the Wheel of Fortune!\n')

def main():
    gameSetup()    

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()