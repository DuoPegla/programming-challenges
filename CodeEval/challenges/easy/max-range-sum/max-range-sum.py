import sys


def calculate_max_gain(num_of_days, report):
    max_gain = 0

    i = 0
    while i <= len(report) - num_of_days:
        gain = sum(report[i:i + num_of_days])
        if gain > max_gain:
            max_gain = gain

        i += 1

    return max_gain

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    test = test.strip()
    num_of_days, report = test.split(';')
    num_of_days = int(num_of_days)
    report = report.split(' ')
    report = [int(x) for x in report]

    print calculate_max_gain(num_of_days, report)

test_cases.close()