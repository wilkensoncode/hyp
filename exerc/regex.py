import re

# import nltk

pattern = r"(?<=wilk) Hilarion"
string = "wilk Hilarion"
match = re.search(pattern, string)
print(match and match.group() or "no match")

# You need to define a regexp pattern using assertions that returns a word following a hyphen -.
string = input()
match = re.search(r"(?<=-)\w+", string)
print(match and match.group())

string = input()
pattern = r"(?<=@)\w+"
results = re.search(pattern, string)  # look behind ue search instead of match
print(results)
print(results and results.group())

"""You need to write a program that takes an input string that contains Alex's' 
weekly expenses and returns' 
 how much he's spent this week. Pay attention to the input and output format in the example."""

string = input()
pattern = r"(?<=\$)\d+"
results = re.findall(pattern, string)
sum_ = sum(map(int, results))
print(f"This week you have spent: {sum_} dollars")
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# need to pip install cltk
sentence = str(input())  # input sentence

# def find_verbs(phrase: str):
#     tokens = nltk.word_tokenize(phrase)  # tokenize the sentence
#     tag_tokens = nltk.pos_tag(tokens)  # POS tagging
#     return [token for token, pos in tag_tokens if pos.startswith('VB')]

# verbs_list = find_verbs(sentence)
# print(verbs_list)


iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {'species': species, 'petal_length': \
        petal_length, 'petal_width': petal_width}
    iris[id_n].update(kwargs)


add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')


# print(iris)


def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    # Get the names of the tallest people sorted alphabetically
    tallest = sorted([name for name, height in kwargs.items() if height == max_height])

    for person in tallest:
        print(f"{person} : {max_height}")


# Test case
tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)


def square_area(side: 'length of square side', number: dict['name': type:int]) -> 'result of side ** 2':
    return side ** 2, number * side * 1.5


print(square_area.__annotations__)  # call annotations attribute

# {'side': 'length of square side', 'return': 'result of side ** 2'}
print(square_area(2, 8))


# def multiplication(a: dict['the multiplicand': type:int],
#                    b: dict['the multiplier': type:int]) \
#         -> dict(description='the result of multiplying a by b', type=int):
#     """Multiply a by b"""
#     return a * b
def func(birth_year: int, current_year: int) -> int:
    return abs(birth_year - current_year)


print(func.__annotations__)

class Account:
    def __init__(self, account_id, amount):
        self.account_id = account_id
        self.amount = amount

    def __iadd__(self, other):
        self.amount += other.amount
        return self

    def __eq__(self, other):
        return ((self.account_id == other.account_id) and
                (self.amount == other.amount))


account1 = Account("acc0000927", 999.99)
account2 = Account("acc0083972", 1564.26)

# print(account1 * account2)
print(account1 == account2)


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __gt__(self, other):
        return self.population > other.population
