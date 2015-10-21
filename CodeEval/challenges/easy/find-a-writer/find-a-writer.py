import sys


def decode(code, key):
    decoded_string = str()

    for i in code:
        decoded_string += key[int(i) - 1]

    return decoded_string

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    key = test.strip().split('|')[0]
    code = test.strip().split('|')[1].strip().split(' ')
    print(decode(code, key))


test_cases.close()