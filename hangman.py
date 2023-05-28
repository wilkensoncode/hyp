import random


def hangman():
    word_choice = ['python', 'java', 'swift', 'javascript']
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
        if guess in word and guess not in guessed:
            for i in range(len(word)):
                if word[i] == guess:
                    res[i] = guess
                    guessed.append(guess)

        else:
            if guess in guessed:
                attempts -= 1
                print(f"No improvements.")
            else:
                attempts -= 1
                print(f"That letter doesn't appear in the word")

        if '-' not in res:
            print(''.join(res))
            print("You guessed the word!")
            print("You survived!")
            break

        print(''.join(res))
        if attempts == 0:
            print("You lost!\nThanks for playing!")
            break
        guess = input(f"Input a letter: ")


hangman()
