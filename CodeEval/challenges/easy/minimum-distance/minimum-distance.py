import sys
import math

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    num_of_friends = int(test.strip().split(' ')[0])
    house_numbers = [int(x) for x in test.strip().split(' ')[1:]]
    house_numbers.sort()

    if num_of_friends % 2 != 0:
        target_house = house_numbers[int(math.floor(float(num_of_friends) / 2))]
    else:
        target_house = house_numbers[num_of_friends / 2] - 1

    distance_sum = 0
    for house in house_numbers:
        distance_sum += abs(target_house - house)

    print distance_sum


test_cases.close()
