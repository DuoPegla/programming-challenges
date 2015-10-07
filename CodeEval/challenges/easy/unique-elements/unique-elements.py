import sys


def remove_duplicates_from_sorted_list(input_list):
    result = list()
    result.append(int(input_list[0]))
    previous = int(input_list[0])

    for i in input_list:
        if int(i) != previous:
            result.append(int(i))
            previous = int(i)

    return result

test_cases = open(sys.argv[1], 'r')
sum = 0
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    sorted_list = remove_duplicates_from_sorted_list(test.strip().split(','))
    output = str()
    for i in sorted_list:
        output += str(i) + ','
    print(output.rstrip(','))

print(sum)

test_cases.close()
