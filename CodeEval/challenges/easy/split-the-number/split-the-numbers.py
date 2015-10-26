import sys


def evaluate(number, pattern):
    if '+' in pattern:
        operator_index = pattern.find('+')
        return int(number[:operator_index]) + int(number[operator_index:])
    else:
        operator_index = pattern.find('-')
        return int(number[:operator_index]) - int(number[operator_index:])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(evaluate(test.strip().split(' ')[0], test.strip().split(' ')[1]))


test_cases.close()

