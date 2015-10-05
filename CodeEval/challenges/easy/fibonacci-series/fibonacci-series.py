import sys


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    previous = 1
    current = 1
    i = 3
    while (i <= n):
        next = previous + current
        previous = current
        current = next
        i += 1

    return current


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(fibonacci(int(test.strip())))

test_cases.close()
