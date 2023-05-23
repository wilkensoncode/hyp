import random

print("H A N G M A N\nThe game will be available soon.")  # stage 1

print("H A N G M A N")  # stage 2
# guess = input("Guess the word:")
# print("You survived!" if guess == "python" else "You lost!")

# stage 3
print("H A N G M A N")
lst = ['python', 'java', 'swift', 'javascript']
choice = random.choice(lst)
guess = input("Guess the word:")
print("You survived!" if guess == choice else "You lost!")