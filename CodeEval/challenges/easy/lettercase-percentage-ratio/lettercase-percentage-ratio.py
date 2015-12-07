import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()

    uppercase_count = 0
    for letter in list(test):
        if letter.isupper():
            uppercase_count += 1

    uppercase_percentage = float(uppercase_count) * 100 / len(test)
    print("lowercase: " + "{0:.2f}".format(100 - uppercase_percentage) +
          " uppercase: " + "{0:.2f}".format(uppercase_percentage))

test_cases.close()

