import sys
import math

CANDY_EFFICIENCY = {"Vampires": 3, "Zombies": 4, "Witches": 5}


def count_candy(data):
    candy_sum = 0
    num_of_children = 0
    for key in data:
        if key != "Houses":
            candy_sum += data[key] * CANDY_EFFICIENCY[key] * data["Houses"]
            num_of_children += data[key]
    return int(math.floor(candy_sum / num_of_children))


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    inputs = test.strip().split(', ')
    data = dict()
    for input in inputs:
        key, value = input.split(': ')
        data[key] = int(value)

    print count_candy(data)


test_cases.close()