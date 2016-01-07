import sys


def compare_points(point1, point2):
    direction = str()

    if point1[1] < point2[1]:
        direction += 'N'
    elif point1[1] > point2[1]:
        direction += 'S'

    if point1[0] < point2[0]:
        direction += 'E'
    elif point1[0] > point2[0]:
        direction += 'W'

    if direction:
        return direction
    else:
        return "here"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    coordinates = [int(x) for x in test.strip().split(' ')]
    point1 = coordinates[0:2]
    point2 = coordinates[2:]

    print compare_points(point1, point2)

test_cases.close()
