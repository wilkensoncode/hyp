import sys

sys.setrecursionlimit(10000)

"""def match_regex(input_str):
    regex, string = input_str.split('|')
    regex_length = len(regex)
    string_length = len(string)

    for i in range(string_length - regex_length + 1):
        if match_equal_length(regex, string[i:i + regex_length]):
            return True

    return False


def match_equal_length(regex, string):
    if regex == '':
        return True
    elif regex[0] == string[0] or regex[0] == '.':
        return match_equal_length(regex[1:], string[1:])
    else:
        return False"""


def match_regex_pair(input_str):
    regex, string = input_str.split('|')
    if regex.startswith('^') and regex.endswith('$'):
        return match_exact(regex[1:-1], string)
    elif regex.startswith('^'):  # Check if regex starts with '^'
        return match_beginning(regex[1:], string)
    elif regex.endswith('$'):  # Check if regex ends with '$'
        return match_end(regex[:-1], string)
    else:
        return match_regex(regex, string)


def match_beginning(regex, string):
    if regex == '':
        return True
    elif string == '':
        return False
    elif regex[0] == string[0] or regex[0] == '.':
        return match_beginning(regex[1:], string[1:])
    else:
        return False


def match_end(regex, string):
    if regex == '':
        return True
    elif string == '':
        return False
    elif regex[-1] == string[-1] or regex[-1] == '.':
        return match_end(regex[:-1], string[:-1])
    else:
        return False


def match_exact(regex, string):
    if regex == string:
        return True
    else:
        return False


def match_regex(regex, string):
    if regex == '':
        return True
    elif string == '':
        return False
    elif regex[0] == string[0] or regex[0] == '.':
        return match_regex(regex[1:], string[1:])
    elif regex.startswith(string):  # Check if input string contains the regex
        return True
    elif match_regex(regex, string[1:]):  # Recursively check the remaining substring
        return True
    else:
        return False


# Test cases
print(match_regex_pair('^app|apple'))  # Output: True
print(match_regex_pair('le|apple'))  # Output: True
print(match_regex_pair('^apple|apple'))  # Output: True
print(match_regex_pair('apple$|apple'))  # Output: True
print(match_regex_pair('^apple$|apple'))  # Output: True
print(match_regex_pair('apple$|pineapple'))  # Output: False
print(match_regex_pair('^apple|pineapple'))  # Output: False

"""
print(match_regex('apple|apple'))  # Output: True
print(match_regex('ap|apple'))  # Output: True
print(match_regex('le|apple'))  # Output: True
print(match_regex('a|apple'))  # Output: True
print(match_regex('.|apple'))  # Output: True
print(match_regex('apwle|apple'))  # Output: True
print(match_regex('peach|apple'))  # Output: True"""

# print(match_regex_pair('apple | apple'))  # Output: True
# print(match_regex_pair('.pple | apple'))  # Output: True
# print(match_regex_pair('appl. | apple'))  # Output: True
# print(match_regex_pair('..... | apple'))  # Output: True
# print(match_regex_pair('peach | apple'))  # Output: False
# print(match_regex_pair('a | a'))  # Output:
