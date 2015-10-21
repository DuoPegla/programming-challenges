import sys


def is_even(number):
    if number % 2 == 0:
        return 1
    else:
        return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    number = int(test.strip())
    print(is_even(number))


test_cases.close()
