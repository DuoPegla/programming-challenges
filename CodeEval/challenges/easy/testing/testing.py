import sys


def test_for_bugs(test_result, expected_result):
    bugs = 0
    for i in xrange(len(test_result)):
        if test_result[i] != expected_result[i]:
            bugs += 1

    if bugs == 0:
        return "Done"
    elif 0 < bugs <= 2:
        return "Low"
    elif 2 < bugs <= 4:
        return "Medium"
    elif 4 < bugs <= 6:
        return "High"
    else:
        return "Critical"


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test_result, expected_result = test.strip().split(' | ')

    print test_for_bugs(test_result, expected_result)


test_cases.close()