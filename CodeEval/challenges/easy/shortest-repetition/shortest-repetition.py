import sys


def shortest_repetition(string):
    substring = str()
    for letter in string:
        substring += letter
        if len(string) % len(substring) != 0:
            continue

        if substring * (len(string) / len(substring)) == string:
            return len(substring)

    return len(string)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(shortest_repetition(test.strip()))


test_cases.close()

