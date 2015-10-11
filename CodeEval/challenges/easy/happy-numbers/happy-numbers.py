import sys


def digit_square_sum(number):
    digits = list(str(number))
    sum = 0
    for digit in digits:
        sum += int(digit) ** 2

    return sum


def is_happy_number(number):
    sums = list()

    while True:
        current_sum = digit_square_sum(number)
        if current_sum == 1:
            return 1
        elif current_sum in sums:
            return 0
        else:
            sums.append(current_sum)
            number = current_sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test:
        continue

    test = test.strip()
    print(is_happy_number(int(test)))

test_cases.close()
