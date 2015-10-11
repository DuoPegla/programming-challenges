import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test:
        continue

    test = test.strip()
    string = test.split(',')[0]
    character = test.split(',')[1]
    print(string.rfind(character))


test_cases.close()