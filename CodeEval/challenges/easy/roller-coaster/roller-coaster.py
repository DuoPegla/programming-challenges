import sys


def roller_coaster_case(input_string):
    output_string = list(input_string)
    j = 0
    for i in range(0, len(output_string)):
        if output_string[i].isalpha():
            if j % 2 != 0 and output_string[i].isupper():
                output_string[i] = output_string[i].lower()
            elif j % 2 == 0 and output_string[i].islower():
                output_string[i] = output_string[i].upper()
            j += 1

    return "".join(output_string)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print roller_coaster_case(test)


test_cases.close()