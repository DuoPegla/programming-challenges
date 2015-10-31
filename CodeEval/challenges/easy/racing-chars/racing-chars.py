import sys


def race(current_position, racetrack):
    target_position = 0
    if 'C' in racetrack:
        target_position = racetrack.find('C')
    elif '_' in racetrack:
        target_position = racetrack.find('_')

    path = list(racetrack)
    # start of race
    if current_position < 0 or current_position == target_position:
        path[target_position] = '|'
    elif target_position == current_position - 1:
        path[target_position] = '/'
    elif target_position == current_position + 1:
        path[target_position] = '\\'

    return target_position, "".join(path)

test_cases = open(sys.argv[1], 'r')
current_position = -1

for test in test_cases:
    if not test:
        continue
    racetrack = test.strip()
    current_position, path = race(current_position, racetrack)
    print (path)

test_cases.close()
