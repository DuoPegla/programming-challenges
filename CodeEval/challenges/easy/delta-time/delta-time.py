import sys


def delta_time(time1, time2):
    time1 = [int(x) for x in time1.split(':')]
    time2 = [int(x) for x in time2.split(':')]

    seconds1 = time1[0] * 3600 + time1[1] * 60 + time1[2]
    seconds2 = time2[0] * 3600 + time2[1] * 60 + time2[2]

    delta_seconds = abs(seconds2 - seconds1)

    result = "{:02d}".format(delta_seconds / 3600) + ':'
    delta_seconds -= (delta_seconds / 3600) * 3600
    result += "{:02d}".format(delta_seconds / 60) + ':'
    delta_seconds -= (delta_seconds / 60) * 60
    result += "{:02d}".format(delta_seconds)

    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print(delta_time(test.split(" ")[0], test.split(" ")[1]))


test_cases.close()
