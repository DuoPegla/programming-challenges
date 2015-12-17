import sys


def read_more_compress(text, max_length):
    if len(text) <= max_length:
        return text

    text = text[0:40]

    if text.rfind(' ') != -1:
        text = text[0:text.rfind(' ')]

    text += "... <Read More>"

    return text

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()

    print(read_more_compress(test, 55))


test_cases.close()