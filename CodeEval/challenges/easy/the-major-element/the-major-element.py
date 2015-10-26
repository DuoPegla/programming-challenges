import sys


def major_element(sequence):
    element_frequency = dict()
    for element in sequence:
        if element not in element_frequency.keys():
            element_frequency[element] = 1
        else:
            element_frequency[element] += 1

    for key in element_frequency.keys():
        if element_frequency[key] > float(len(sequence)) / 2:
            return key

    return 'None'

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(major_element(test.strip().split(',')))


test_cases.close()

