import sys


def swap_case(sentence):
    letters = list(sentence)

    for i in range(len(letters)):
        if not letters[i].isalpha():
            continue

        if letters[i].islower():
            letters[i] = letters[i].upper()
        else:
            letters[i] = letters[i].lower()

    return "".join(letters)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(swap_case(test.strip()))

test_cases.close()