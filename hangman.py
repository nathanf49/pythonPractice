#!/usr/bin/python
def wordProgress(solution, guessedLetters): #function to print the letters the user has guessed
    show = []
    for letter in solution:
        if letter in guessedLetters:
            show.append(letter) #appends letter if it has been guessed
        else:
            show.append('_') #appends underscore if not
    return(show)

def printHangman(guesses): #function to print the hangman design
    if guesses == 0:
        return(' ----|\n     |\n     |\n     |\n   __|__')
    elif guesses == 1:
        return(' ----|\n O   |\n     |\n     |\n   __|__')
    elif guesses == 2:
        return(' ----|\n O   |\n |   |\n     |\n   __|__')
    elif guesses == 3:
        return(' ----|\n O   |\n/|   |\n     |\n   __|__')
    elif guesses == 4:
        return(' ----|\n O   |\n/|\  |\n     |\n   __|__')
    elif guesses == 5:
        return(' ----|\n O   |\n/|\  |\n/    |\n   __|__')
    elif guesses == 6:
        return(' ----|\n O   |\n/|\  |\n/ \  |\n   __|__')

def hangman(solution):
    validLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    solutionLetters = []
    for letter in solution: #Creates list of letters in the input word
        if letter in validLetters:
            if letter not in solutionLetters:
                solutionLetters.append(letter)

    guessedLetters = [] #keeps a list of letters that have been guessed to avoid repeats
    guesses = 0
    print(printHangman(guesses)) #prints empty figure at start
    while guesses <= 5 and len(solutionLetters) != 0: #breaks at 6(max) guesses or when all letters are guessed
        print(wordProgress(solution,guessedLetters)) #prints progress on each loop
        guess = input('Please enter a guess as a single letter:\n').lower()
        if len(guess) != 1: #checks that user only inputs one letter at a time
            print('\nPlease only enter 1 letter at a time.\n')
        else:
            if guess in validLetters:
                if guess in guessedLetters: #prevents user from guessing the same letter more than once
                    print('\nYou already guessed that letter.\n')
                else:
                    guessedLetters.append(guess) #if letter hasn't been guessed, it is added to list of guessed guessedLetters
                    if guess in solutionLetters:
                        solutionLetters.remove(guess) #removes guessed letter to end while loop
                    else:
                        guesses += 1
            else:
                print("That doesn't seem to be a valid guess. Please guess a letter")
        print(printHangman(guesses)) #prints figure on each loop

    if guesses == 6: #player loses if they get to 6 guesses
        print(printHangman(guesses)) # prints last image since loop will break before it prints
        show = wordProgress(solution,guessedLetters)
        misses = 0
        for letter in show: #counts how close the player was to winning
            if letter == '_':
                misses += 1
        return(misses, False)

    else: #Display word and congratulations message
        return(0, True)

solution = input('Please enter a word for another player to guess:\n')
solution = solution.lower() #converts to all lowercase letters

misses,win = hangman(solution)
if win == False:
    print('The word was:', solution) #outputs loss message
    if misses == 1:
        print('Sorry, you lose. You only missed', misses, 'letter. Better luck next time!')
    else:
        print('Sorry, you lose. You only missed', misses, 'letters. Better luck next time!')
else:
    print('Congratulations! You win!')
