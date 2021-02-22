
import random 
# This is used to randomly chose an item from a list [] 
import time
# This is used to import the actual time from pc to program

# Invite the user to start the game
print("\nWelcome to Hangman!\n")
name = input("Enter your name: ")
print("Hello " + name + "! Good luck.")
time.sleep(2)
# time.sleep() is used to halt the execution of the program for a few seconds.
print("The game is about start!\nLet's play Hangman!")
time.sleep(3)

# Define the main() function of the game to be called later
def main():
    global count
    global display
    global word
    global already_guessed
    global length 
    words_to_guess = ["chance", "turn", "exclusive", "harbor", "official", "wage", "fabricate" , "extend", "lazy" , "page" , "plead" , "location" , "variation" , "reach"]
    # contains strings of all words available to user
    word = random.choice(words_to_guess)
    # use the random module on this variable to randomly chose from words_to_guess
    length = len(word)
    # len() helps to get length of the string
    count = 0
    # initialised to 0 and will increment later in the game
    display = "_" * length
    # this will draw the lines of the word_to_guess for us
    already_guessed = []
    # contain the string indices of the correctly guessed words
    play_again = ""

# Create a loop to continously execute the game
def game_loop():
    global play_again
# Use a variable to continue or exit the game, depending on user input
    play_again = input("Do you want to play again? Answer 'yes' or 'no'\n")
# Use a while loop to execute the play_again variable. Cover user input error   
    while play_again not in ["yes", "no", "y", "n","YES", "NO"]:
        play_again = input("Do you want to play again? Answer 'yes' or 'no'\n")
    if play_again == "yes" or play_again == "y" or play_again == "YES":
        main()
    elif play_again == "n" or play_again == "no" or play_again == "NO":
        print(" Thanks for playing Hangman! See you soon.")
        exit()

# Create the conditions for Hangman through a function
# call global variables from main()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_againg
    limit = 5
    guess = input("Guess the word: "+ display + " Guess a letter: \n")
    guess = guess.strip()
    # Use if/elif/else statements to determine which letters are in the hangman word and which are not.
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
    # If letter is correctly guessed, index searches for that letter in the word
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
    # Display places the letter in the given space according to the index and where it belongs in the word
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1
    # if letter is not in word, increment count and start printing hangman. limit = 5
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
        # Show player the word they failed to guess
            print("The word was:",already_guessed,word)
        # Loop again to restart game
            game_loop()
    # Winning/losing conditions
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        game_loop()

    elif count != limit:
        hangman()


main()

hangman()


