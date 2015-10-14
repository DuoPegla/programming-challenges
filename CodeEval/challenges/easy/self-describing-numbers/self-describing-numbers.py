import sys


def is_self_describing_number(number):
    actual_frequency = dict()
    target_frequency = dict()

    digits = list(str(number))
    for i in range(len(digits)):
        if i < 10:
            target_frequency[str(i)] = int(digits[i])

        if digits[i] not in actual_frequency.keys():
            actual_frequency[digits[i]] = 1
        else:
            actual_frequency[digits[i]] += 1

    for key in target_frequency.keys():
        if key in actual_frequency.keys():
            if target_frequency[key] != actual_frequency[key]:
                return 0
        else:
            if target_frequency[key] > 0:
                return 0

    return 1



test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(is_self_describing_number(int(test.strip())))


test_cases.close()