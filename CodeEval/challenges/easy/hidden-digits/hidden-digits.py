import sys


HIDDEN_DIGITS = {
    'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4',
    'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9',
}


def find_hidden_digits(message):
    digits = str()
    for character in list(message):
        if character in HIDDEN_DIGITS.keys():
            digits += HIDDEN_DIGITS[character]

        if character.isdigit():
            digits += character

    if len(digits) == 0:
        return "NONE"
    else:
        return digits

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(find_hidden_digits(test.strip()))


test_cases.close()
