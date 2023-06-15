import random


def generate_word():
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "melon"]
    word = random.choice(words)
    return word


def get_guess():
    guess = input("Guess a word: ")
    return guess.lower()


def evaluate_guess(word, guess):
    if guess == word:
        return "Congratulations! You guessed correctly."

    # 'O' for correct letter in correct position, 'X' for correct letter in wrong position
    result = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            result += "O"
        elif guess[i] in word:
            result += "X"
        else:
            result += "_"

    return result


def play_game():
    word = generate_word()
    attempts = 0
    max_attempts = 5

    print("Welcome to the Word Guessing Game!")
    print("Enter your guesses in lowercase letters.")
    print("_ " * len(word))

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1
        result = evaluate_guess(word, guess)

        print(result)

        if result == "Congratulations! You guessed correctly.":
            break

    if attempts == max_attempts:
        print(f"You ran out of attempts. The correct word was '{word}'.")


play_game()
