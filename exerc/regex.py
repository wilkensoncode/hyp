import re

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
