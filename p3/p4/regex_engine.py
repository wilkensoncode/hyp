def match_regex_pair(input_str):
    regex, string = input_str.split('|')
    if regex == '':
        # All characters in the regex have been consumed
        return True
    elif string == '':
        # The input string has been fully consumed, but the regex is not
        return False
    elif regex[0] == string[0] or regex[0] == '.':
        # First character of the regex matches the first character of the string
        # ,or it is a wildcard character ('.')
        return match_regex_pair(regex[1:] + '|' + string[1:])
    else:
        # First character of the regex doesn't match the first character of the string
        return False


print(match_regex_pair('apple | apple'))  # Output: True
print(match_regex_pair('.pple | apple'))  # Output: True
print(match_regex_pair('appl. | apple'))  # Output: True
print(match_regex_pair('..... | apple'))  # Output: True
print(match_regex_pair('peach | apple'))  # Output: False
print(match_regex_pair('a | a'))  # Output: False



