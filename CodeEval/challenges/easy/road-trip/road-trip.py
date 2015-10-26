import sys


def road_trip(distances):
    distances.sort()
    current_distance = 0
    trip_distances = list()

    for d in distances:
        trip_distances.append(d - current_distance)
        current_distance = d

    return trip_distances

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    distances = list()

    for city_distance in test.strip().rstrip(';').split('; '):
        distances.append(int(city_distance.split(',')[1]))

    result = str()
    for distance in road_trip(distances):
        result += str(distance) + ','
    result = result.rstrip(',')
    print(result)


test_cases.close()