import sys


def roman_numerals(decimal_number):
	roman_number = str()
	thousands = decimal_number / 1000
	roman_number += thousands * 'M'

	houndreds = (decimal_number % 1000) / 100
	if 0 < houndreds < 4:
		roman_number += houndreds * 'C'
	elif houndreds == 4 or houndreds == 5:
		roman_number += (5 - houndreds) * 'C' + 'D'
	elif 5 < houndreds < 9:
		roman_number += 'D' + (houndreds - 5) * 'C'
	elif houndreds == 9:
		roman_number += 'CM'

	tens = (decimal_number % 100) / 10
	if 0 < tens < 4:
		roman_number += tens * 'X'
	elif tens == 4 or tens == 5:
		roman_number += (5 - tens) * 'X' + 'L'
	elif 5 < tens < 9:
		roman_number += 'L' + (tens - 5) * 'X'
	elif tens == 9:
		roman_number += 'XC'

	ones = decimal_number % 10
	if 0 < ones < 4:
		roman_number += ones * 'I'
	elif ones == 4 or ones == 5:
		roman_number += (5 - ones) * 'I' + 'V'
	elif 5 < ones < 9:
		roman_number += 'V' + (ones - 5) * 'I'
	elif ones == 9:
		roman_number += 'IX'

	return roman_number

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(roman_numerals(int(test.strip())))

test_cases.close()
