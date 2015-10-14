import sys


def hex_to_decimal(hex):
    return int(hex, 16)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(hex_to_decimal(test.strip()))


test_cases.close()
