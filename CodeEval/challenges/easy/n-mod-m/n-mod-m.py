import sys


def modulo(n, m):
    return n - m * (n/m)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    n = test.strip().split(',')[0]
    m = test.strip().split(',')[1]
    print(modulo(int(n), int(m)))


test_cases.close()