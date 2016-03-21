import sys


def clean_words(string):
    clean_string = str()
    is_word = False
    for i in string:
        if i.isalpha():
            if not is_word:
                is_word = True
                clean_string += ' '
            clean_string += i.lower()

        else:
            is_word = False

    return clean_string.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print clean_words(test.strip())


test_cases.close()