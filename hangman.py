import random


def hangman():
    # 'python', 'javascript', 'swift',
    word_choice = ['java']
    choice = random.choice(word_choice)
    dont_die(choice)


def dont_die(word: str):
    attempts = 8
    print(f"H A N G M A N")
    res = ['-'] * len(word)  # initialize array with dashes
    guessed = []
    print(''.join(res))

    guess = input(f"Input a letter: ")
    while attempts > 0:
        if not guess.islower() and len(guess) == 1:
            print("Please, enter a lowercase letter from the English alphabet.")
        elif len(guess) != 1:
            print("Please, input a single letter.")
        elif guess in word and guess not in guessed:
            for i in range(len(word)):
                if word[i] == guess:
                    res[i] = guess
                    guessed.append(guess)

        else:
            if guess in guessed:
                print("You've already guessed this letter.")
            else:
                attempts -= 1
                print(f"That letter doesn't appear in the word.")
            guessed.append(guess)

        if '-' not in res:
            print(f"You guessed the word {''.join(res)}!")
            print("You survived!")
            break

        print(''.join(res))
        if attempts == 0:
            print("You lost!\nThanks for playing!")
            break
        guess = input(f"Input a letter: ")


hangman()
