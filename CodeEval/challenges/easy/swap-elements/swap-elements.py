import sys


def swap_elements(numbers, pos1, pos2):
    temp = numbers[pos1]
    numbers[pos1] = numbers[pos2]
    numbers[pos2] = temp
    return numbers

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    numbers = test.strip().split(' : ')[0].split(' ')
    positions = test.strip().split(' : ')[1].split(', ')
    swapped_list = list(numbers)

    for position in positions:
        swapped_list = swap_elements(swapped_list, int(position.split('-')[0]), int(position.split('-')[1]))

    print " ".join(swapped_list)

test_cases.close()
