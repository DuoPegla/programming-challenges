import sys


def text_to_number(digit_strings):
	number = str()
	for digit in digit_strings:
		if digit == "zero":
			number += '0'
		elif digit == "one":
			number += '1'
		elif digit == "two":
			number += '2'
		elif digit == "three":
			number += '3'
		elif digit == "four":
			number += '4'
		elif digit == "five":
			number += '5'
		elif digit == "six":
			number += '6'
		elif digit == "seven":
			number += '7'
		elif digit == "eight":
			number += '8'
		elif digit == "nine":
			number += '9'

	return number

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(text_to_number(test.strip().split(';')))

test_cases.close()
