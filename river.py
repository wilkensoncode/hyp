 
class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.length)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}!"


person = Person(input())
print(person.greet())


def calculate(amount, interest_rate, time):
    interest = amount * interest_rate * time / 100
    total_amount = amount + interest
    return interest, total_amount


def print_result(interest, total_amount):
    print(f"The interest is: {interest}\nThe total amount is: {total_amount}")
