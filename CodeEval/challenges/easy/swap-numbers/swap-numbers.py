import sys


def swap_numbers(sentance):
    swapped = str()
    for word in sentance.split(' '):
        swapped += word[-1] + word[1:-1] + word[0]
        swapped += ' '
    return swapped.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print swap_numbers(test.strip())

test_cases.close()
