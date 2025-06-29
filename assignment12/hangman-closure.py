def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        masked_character = []
        for char in secret_word:
            if char in guesses:
                masked_character.append(char)
            else:
                masked_character.append("_")
        masked_word = "".join(masked_character)

        print(masked_word)
        if masked_word == secret_word:
            return True
        else:
            return False

    return hangman_closure


secret = input("Enter the secret word: ")

game = make_hangman(secret)

while True:
    letter = input("Guess a letter: ")
    done = game(letter)
    if done:
        print("You guessed the word!")
        break
