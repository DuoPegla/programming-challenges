import sys

LEFT_ARROW = "<--<<"
RIGHT_ARROW = ">>-->"


def find_arrow_count(string):
    arrows_found = 0
    for i in xrange(len(string)):
        if string[i:i+len(LEFT_ARROW)] == LEFT_ARROW or string[i:i+len(RIGHT_ARROW)] == RIGHT_ARROW:
            arrows_found += 1

    return arrows_found

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print find_arrow_count(test.strip())


test_cases.close()