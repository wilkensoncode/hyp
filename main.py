import re

regexp = '..ever gonna'
string = '\\'
result = re.match(r"\\", string)
print(result)
