import sys


def sum_of_digits(number):
    number = str(number)
    sum = 0
    for i in number:
        sum += int(i)
    return sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(sum_of_digits(test.strip()))

test_cases.close()