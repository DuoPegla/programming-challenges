import sys


def count_zeros(num_of_zeros, sequence):

    found_numbers = 0
    for number in sequence:
        if bin(number).split('b')[1].count('0') == num_of_zeros:
            found_numbers += 1

    return found_numbers


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    num_of_zeros = int(test.strip().split(' ')[0])
    sequence = range(1, int(test.strip().split(' ')[1])+1)

    print count_zeros(num_of_zeros, sequence)


test_cases.close()