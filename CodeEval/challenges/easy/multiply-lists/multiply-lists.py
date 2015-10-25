import sys


def multiply_lists(list1, list2):
    result = list()
    for i in range(len(list1)):
        result.append(str(int(list1[i]) * int(list2[i])))
    return result


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    list1 = test.strip().split(' | ')[0].split(' ')
    list2 = test.strip().split(' | ')[1].split(' ')

    print(" ".join(multiply_lists(list1, list2)))


test_cases.close()
