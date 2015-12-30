import sys
from collections import Counter


def major_element(sequence):
    count = Counter(sequence)

    if count.most_common(1)[0][1] > (len(sequence)/2):
        return count.most_common(1)[0][0]
    else:
        return 'None'

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(major_element(test.strip().split(',')))


test_cases.close()

