import random

words = ["apple", "banana", "grapes", "kiwi", "watermelon", "dragon fruit"]

secret_word = random.choice(words)
guessing_word = ["_"] * len(secret_word)

word_guessed = 0
max_chance = 6

print("---- HANGMAN GAME ----")

while word_guessed < max_chance and "_" in guessing_word:
    print("\nCurrent Word:", " ".join(guessing_word))
    guess = input("enter the letter: ")

    if guess in secret_word:
        print("correct guess")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessing_word[i] = guess

    else:

        word_guessed += 1

        print ("wrong guess")
        print("remaining guess: ", max_chance - word_guessed)

    if "_" not in guessing_word:
        print("congratulation")
        print("you guessed the word: ", secret_word)

    else:

        print("\n game over")
        print("the correct word was: ", secret_word)