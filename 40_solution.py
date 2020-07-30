import random,re#import the random and regular expression function


"""Function one: is_secret_guessed"""
def is_secret_guessed(secret_word, letters_guessed):
    #Here I Convert our secret word to a list of characters.
    #Because our letters_guessed is also a list of characters.
    #this makes it easier to compare them.
    secret_word = list(secret_word) #I have made a list for the secret word

    for char in range(len(secret_word)):# This loop iterates through all the characters in out secret word

        char = secret_word[0]#We set out character to the first index of our secret_word.

        if secret_word[0] in letters_guessed: #We check if the character is in the array 'letters_guessed' If it is, then we remove both the characters from the lists.
            secret_word.remove(char) #Removing the character from the list
    # After it has checked all characters, we check if it has removed
    # all characters and secret_word would be an empty list now.
    if secret_word == []: #If secret word is in the list
        return True #Return true if it is
    else:
        return False #otherwise return false

"""Function two: get_current_guess"""
def get_current_guess(secret_word, letters_guessed): #Declaring a function called get_current_guess with the parameters secret_word and letters_guessed
    return_string = [] #Returns to an empty list

    for char in secret_word: #Loops through secret word with every character
        if char in letters_guessed: #If the character that is in the list letter_guessed
            return_string.append(char) #adds that character to our return string
        else:
            return_string.append("_") # if character is not in list it adds a '-' character to our return string
    return return_string #Return the list


"""Function three: first_game"""
def first_game(secret_word):
    """ User gets 5 extra guesses than letters in our word
     Current guess creates our "-a--d-"-like string. then every time, we check
     if the word has been guessed with our is_secret_guessed() function.
     After that, our guesses get decremented by 1."""

    guesses = len(secret_word) + 5 #The amount of guesses given to the user is the length of the secret word + 5
    letters_guessed = [] #Making an empty list for the letters guessed by the user
    while(guesses > 0): #While the guesses left are at least one..
        print ("You have {} guesses.".format(guesses)) #Printing the remaining guesses
        char =input("Guess a character in the secret word: ") #Taking an input from the user for a letter
        if len(char)!=1 or not char.isalpha(): #If the character entered is not equal to a length of 1 or its not alpha then...
            print("Only one letter can input and only alpha accept") #Print this statement if the if statement is true
        else:
            letters_guessed += char #Letters_guessed list now contains the character the user inputs each time
            current_guess = get_current_guess(secret_word, letters_guessed) #The current guess is now stored
            print ("The partially guessed word is: {}".format(''.join(current_guess))) #Outputs the current partially guessed word
            if is_secret_guessed(secret_word, letters_guessed): #If the words guessed that are put in the list matches the secret word
                print ("Its a win") #Print if the statement is true
                return (0) #This ends the game
            guesses -= 1 #Reducing the guesses by 1 each time
            if guesses == 0: #If the user has no more guesses
                print("You have lost!!, so the word was",secret_word) #Print a loss message

"""Function three: load_words
load_words, which takes in the file name and returns the list of
words and their count (number of words in the file)."""

def load_words(filename):#this is the function to load the words from the list and its name load_words
    try: #Use of exception handling, opening and reading a file
        words_file=open(filename, "r")#this is to open the file and read the document
        all_words=words_file.read() #This reads the document and puts it into another variable
    except (IOError,ValueError):#to check is there any IOError when we import the file
        print("something went wrong when waiting the file") #Raising the exception to alert the user
    finally:
        words_file.close()#after the file has been read it will finally close it
        all_words=all_words.split()#split the word into another line
    try:#use try function to ensure all the index are correct
        all_words=[i.strip(' ') for i in all_words]#remove both sides space of a word in the list
    except IndexError: #Raising an exception for IndexError
        print("index not found in sequence") #Output message for IndexError
    else:
        all_words=list(filter(lambda x : x!= '',all_words))#Remove all the empty words out
    return [len(all_words),all_words]#Return all the words into a list and count how many words are in the list


"""choose_secret_word, which takes in no argument and returns a
word selected at random from the list of words."""


def choose_secret_word():#this is the function to choose a secret word from the list
    try: #Executing the first part of the code
        load_words_var=load_words("words.txt")#Loading the words from the txt file by making a variable equal to the txt file
        word=random.choice(load_words_var[1])#it is a random function to choose the word
        print("The total amount in word list is",load_words_var[0])#Printing the total amount of words in the word list
    except (IOError,ImportError) as error:#check if the file can import to the program or not
        print(error) #Printing a error message to user
    return(word)#return the word into a function

"""second_game, which calls the first_game and returns the outcome 'win' or 'lose, it also choses a secret word at random that is given in the txt file'"""

def second_game():
    secret_word = choose_secret_word() #making the secret word equal to the function choose secret word which picks a secret word in txt file at random
    if first_game(secret_word)==0: #if the secret word is equal to the return statement of 0
        return("win") #return the win result


"""game_stats, It's a function to find out the average win rate and allows the user to play a number of times as well as giving the total win and lose decription
    created our data structure as dictionary
    table = dict.fromkeys(['win','lose','average'])"""

def game_stats(times): #function showing game statistics
    table = {'win':0,'lose':0} #dictionary table created for win and lose
    for i in range(times): # we'll loop depending on the number of times
        if second_game() == "win": #if the user guesses the correct word and has win as an output
            table['win'] += 1 #Increase the win counter by 1
        else:
            table['lose'] += 1 #Reduce the lose counter by 1 if the win counter didn't get incremented
    return (table,table["win"]/times*100) #finding the average by the calculation, using return for the table


secret_word = "Emmanuel" #The word that is needed to be guessed by the user to win
first_game(secret_word)#run the first game

try:
    times = int(input("Please enter how many times you want to play:")) #This gets the input of user of the number of times they want to play for second game
    if times <= 0: #if the number of times chosen is less than or equal to 0...
        print("Enter a positive number") #print enter a positive number
except ValueError: #If the input cannot be evaluated as an int then an exception is raised
    print("Please enter the valid number") #If the condition is not true then this will be printed


print(game_stats(times))
