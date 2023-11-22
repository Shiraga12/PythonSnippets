def concatenate(str1, str2):
    return str1 + str2
def reverse(string):
    return string[::-1]
def capitalize(string):
    return string.capitalize()
def count_occurrences(string, substrings):
    count = 0
    if len(substrings) > 1:
        for substring in substrings:
            count += string.count(substring)
        return count
    else:
        return string.count(substrings)
def is_palindrome(string):
    return string == string[::-1]
def remove_whitespace(string):
    return string.replace(" ", "")
def convert_to_uppercase(string):
    return string.upper()
def convert_to_lowercase(string):
    return string.lower()
