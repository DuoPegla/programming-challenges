import sys


def is_armstrong_number(number):
    digits = list(str(number))
    sum = 0
    for digit in digits:
        digit = int(digit)
        sum += digit ** len(digits)

    return sum == int(number)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    number = test.strip()
    print(is_armstrong_number(number))


test_cases.close()