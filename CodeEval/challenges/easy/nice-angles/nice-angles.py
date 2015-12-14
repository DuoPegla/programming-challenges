import sys


def format_angle(angle):
    degrees = int(angle)
    minutes = (angle - degrees) * 60
    seconds = (minutes - int(minutes)) * 60

    return str(degrees) + "." + '{0:02}'.format(int(minutes)) + "'" + '{0:02}'.format(int(seconds)) + '"'


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print(format_angle(float(test)))


test_cases.close()