
def print_input_error():
    print("# Invalid input! Try again!")


def create_secret_string(word):
    secret_word = ""
    for c in word:
        secret_word += "_"
    return secret_word


def update_secret_word(letter, word, secret_word):
    pos = 0
    for c in word:
        if letter == c:
            secret_word = secret_word[:pos] + letter + secret_word[pos + 1:]
        pos += 1

    return secret_word


def hangman_game():
    word = "computer"
    secret_word = create_secret_string(word)
    guesses = 10
    entered_letters = []
    win = False
    i = 1
    while guesses > 0 and not win:
        print("\nRound " + str(i))
        print("----------------------")
        print("Guesses left: " + str(guesses))
        print("Entered letters: " + str(entered_letters))
        print("Word status: " + secret_word)
        c = input("Enter a letter:\n")
        guesses -= 1
        if not c.isalpha() or len(c) > 1:
            print_input_error()
            continue
        if c in entered_letters:
            print("# You entered that letter before!")
            continue
        entered_letters.append(c)
        secret_word = update_secret_word(c, word, secret_word)

        print("\nWord status: " + secret_word)

        while True:
            user_input = input("Do you know the word? (y/n)\n")
            if user_input == 'n' or user_input == 'N':
                break

            if user_input != 'y' and user_input != 'Y':
                print_input_error()
                continue
        
            answer = input("Enter the word:\n")
            if answer == word:
                win = True
                break
        
        i += 1

    return win
        

def main():
    print("Welcome to the Hangman game!")

    while True:
        user_input = input("Do you want to start the game? (y/n)\n")
        if user_input == 'n' or user_input == 'N':
            break

        if user_input != 'y' and user_input != 'Y':
            print_input_error()
            continue
        
        win = hangman_game()
        
        if win:
            print("Congratulations! You won the game!")
        else:
            print("Sorry! You lost!")
            
    print("Finishing Hangman game... See you soon!")

if __name__ == "__main__":
    main()