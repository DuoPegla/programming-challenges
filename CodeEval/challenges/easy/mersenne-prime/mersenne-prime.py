import sys


MERSENNE_NUMBERS = [3, 7, 31, 127, 2047]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    result = list()
    for i in MERSENNE_NUMBERS:
        if i > int(test.strip()):
            break
        result.append(str(i))

    print ", ".join(result)

test_cases.close()
