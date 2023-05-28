import random


def hangman():
    # 'python', 'javascript', 'swift','python'
    word_choice = ['java']
    choice = random.choice(word_choice)
    dont_die(choice)


def dont_die(word: str):
    attempts = 8
    print(f"H A N G M A N")
    # number of wins / lost
    win = 0
    lose = 0
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    while True:
        if decision == "exit":
            print()
            break
        elif decision == 'results':
            print(f"You won: {win} times.")
            print(f"You lost: {lose} times.")
        elif decision == 'play':
            guessed = []
            print()
            res = ['-'] * len(word)
            print(''.join(res))
            while attempts > 0:
                guess = input(f"Input a letter: ")
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
                    win += 1
                    print(win)
                    print(f"You guessed the word {''.join(res)}!")
                    print("You survived!")
                    break

                print(''.join(res))
                if attempts == 0:
                    lose += 1
                    print(lose)
                    print("You lost!\nThanks for playing!")
                    break
                # guess = input(f"Input a letter: ")
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')


hangman()