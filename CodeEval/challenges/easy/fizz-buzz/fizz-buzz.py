import sys


def generate_fb(first_divider, second_divider, n):
    result = str()
    for i in range(1, n + 1):
        if i % first_divider == 0 and i % second_divider == 0:
            result += 'FB'
        elif i % first_divider == 0:
            result += 'F'
        elif i % second_divider == 0:
            result += 'B'
        else:
            result += str(i)

        result += ' '

    return result.strip()


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    params = test.split(' ')
    first_divider = int(params[0].strip())
    second_divider = int(params[1].strip())
    n = int(params[2].strip())
    print(generate_fb(first_divider, second_divider, n))

test_cases.close()
