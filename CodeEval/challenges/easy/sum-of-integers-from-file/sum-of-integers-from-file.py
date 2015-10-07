import sys


test_cases = open(sys.argv[1], 'r')
sum = 0
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    sum += int(test.strip())

print(sum)

test_cases.close()