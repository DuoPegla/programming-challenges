import sys


def is_card_valid(card_number):

    control_sum = 0
    for i in xrange(len(card_number)):
        if i % 2 == 0:
            control_sum += card_number[i] * 2
        else:
            control_sum += card_number[i]

    if control_sum % 10 == 0:
        return "Real"
    else:
        return "Fake"


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    number = test.strip()
    card_number = list()
    for digit in number:
        if digit.isdigit():
            card_number.append(int(digit))

    print(is_card_valid(card_number))


test_cases.close()