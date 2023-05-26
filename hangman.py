import random


def main():
    print("H A N G M A N\nThe game will be available soon.")  # stage 1

    print("H A N G M A N")  # stage 2
    # guess = input("Guess the word:")
    # print("You survived!" if guess == "python" else "You lost!")

    # stage 3
    print("H A N G M A N")
    lst = ['python', 'java', 'swift', 'javascript']
    choice = random.choice(lst)

    guess = input(f"Guess the word {show_hint(choice)}:")
    print("You survived!" if guess == choice else "You lost!")


# stage 4
def show_hint(word: str):
    w = []
    for i in range(3):
        w.append(word[i])

    for i in range(len(word) - 3):
        while len(w) < len(word):
            w.append('-')

    return "".join(w)


main()
