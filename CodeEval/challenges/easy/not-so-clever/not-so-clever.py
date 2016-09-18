import sys


def stupid_sort(array, steps):
    steps_done = 0
    while steps_done < steps:
        for i in xrange(len(array)-1):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                steps_done += 1
                break
    return array

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    array = test.split(" | ")[0].strip().split(' ')
    steps = test.split(" | ")[1].strip()

    array = map(int, array)
    steps = int(steps)

    result = stupid_sort(array, steps)
    result = map(str, result)

    print ' '.join(result)


test_cases.close()

