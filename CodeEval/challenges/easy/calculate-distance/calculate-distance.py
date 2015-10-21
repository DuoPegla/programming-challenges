import sys
import math


def distance(point1, point2):
    d = math.sqrt((int(point1[0]) - int(point2[0]))**2 + (int(point1[1]) - int(point2[1]))**2)
    return int(d)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    point1 = test.strip().split(') (')[0].strip('(').split(", ")
    point2 = test.strip().split(') (')[1].strip(')').split(", ")
    print(distance(point1, point2))


test_cases.close()