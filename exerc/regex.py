import re

pattern = r"(?<=wilk) Hilarion"
string = "wilk Hilarion"
match = re.search(pattern, string)
print(match and match.group() or "no match")