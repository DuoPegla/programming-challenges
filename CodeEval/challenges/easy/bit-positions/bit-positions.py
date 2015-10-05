import sys


def is_same_bit(number, position1, position2):
    number_binary = '{0:032b}'.format(number)[::-1]
    if number_binary[position1 - 1] == number_binary[position2 - 1]:
        return "true"
    else:
        return "false"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    params = test.split(',')
    number = int(params[0].strip())
    position1 = int(params[1].strip())
    position2 = int(params[2].strip())
    print(is_same_bit(number, position1, position2))

test_cases.close()
