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

"""
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
"""


def compare(regex, string):
    if not regex or regex == '$' and not string:
        return True
    if len(regex) > 1 and regex[1] in ('?', '*', '+'):
        return quantifiers(regex, string)
    if not string or regex[0] not in (string[0], '.'):
        return False
    return compare(regex[1:], string[1:])


def quantifiers(regex, string):
    if regex[1] in ('*', '+') and len(string) > 1 and (string[0] == string[1] == regex[0] or regex[0] == '.'):
        return (compare(regex[2:], string) if regex[1] != '+' else compare(regex[2:], string[1:])) \
            or compare(regex, string[1:])
    elif string and (regex[0] in (string[0], '.')):
        return regex[1] != '+' and compare(regex[2:], string) or compare(regex[2:], string[1:])
    else:
        return False if regex[1] == '+' else compare(regex[2:], string)


def change_pos(regex, string):
    return compare(regex, string) or bool(string) and change_pos(regex, string[1:])


def check_caret(regex, string):
    return compare(regex[1:], string) if regex.startswith('^') else change_pos(regex, string)


def main():
    data = input().split('|')
    print(check_caret(*data))


