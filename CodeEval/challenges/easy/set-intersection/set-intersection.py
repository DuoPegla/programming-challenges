import sys


def set_intersection(list1, list2):
    intersection = set(list1).intersection(set(list2))
    intersection = list(intersection)
    intersection.sort()
    return intersection

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test:
        continue

    test = test.strip()
    list1 = test.split(';')[0].split(',')
    list2 = test.split(';')[1].split(',')
    result = set_intersection(list1, list2)
    if result:
        print ','.join(result)
    else:
        print ''


test_cases.close()