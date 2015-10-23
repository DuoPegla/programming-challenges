import sys


def lowest_unique_number(numbers):
	numbers = map(int, numbers)

	unique_numbers = dict()
	for i in range(len(numbers)):
		if numbers[i] not in numbers[:i] + numbers[i+1:]:
			unique_numbers[numbers[i]] = i

	lowest_index = 0
	lowest_value = 10
	if len(unique_numbers.keys()) > 0:
		for unique_number in unique_numbers.keys():
			if unique_number < lowest_value:
				lowest_value = unique_number
				lowest_index = unique_numbers[unique_number] + 1

	return lowest_index


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(lowest_unique_number(test.strip().split(' ')))

test_cases.close()
