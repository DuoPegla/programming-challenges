import sys


def compress_sequence(input_sequence):
    current_number = input_sequence[0]
    occurrences = 0
    compressed_sequence = list()

    for i in range(len(input_sequence)):
        if input_sequence[i] == current_number:
            occurrences += 1
        else:
            compressed_sequence.append(str(occurrences))
            compressed_sequence.append(current_number)
            current_number = input_sequence[i]
            occurrences = 1

    compressed_sequence.append(str(occurrences))
    compressed_sequence.append(current_number)

    return compressed_sequence

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(" ".join(compress_sequence(test.strip().split(' '))))

test_cases.close()