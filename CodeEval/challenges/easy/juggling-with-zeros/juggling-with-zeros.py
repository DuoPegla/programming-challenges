import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    digits = test.split(' ')
    binary_number = str()
    for i in range(0, len(digits), 2):
        if digits[i] == "0":
            binary_number += digits[i+1]
        elif digits[i] == "00":
            binary_number += '1' * len(digits[i+1])

    print int(binary_number, 2)

test_cases.close()