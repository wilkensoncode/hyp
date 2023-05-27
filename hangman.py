import random


def hangman_guess():
    word_choice = ['python', 'java', 'swift', 'javascript']
    choice = random.choice(word_choice)
    attempt_guess(choice)


def attempt_guess(word: str):
    attempts = 8
    print(f"H A N G M A N")
    res = ['-'] * len(word)  # initialize array with dashes
    print(''.join(res))

    guess = input(f"Input a letter: ")
    while attempts > 0:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    res[i] = guess
        else:
            print(f"That letter doesn't appear in the word")

        attempts -= 1
        if '-' not in res:
            print(''.join(res))
            print("Thanks for playing!")
            break
        print(''.join(res))
        if attempts == 0:
            print("Thanks for playing!")
            break
        guess = input(f"Input a letter: ")


hangman_guess()
