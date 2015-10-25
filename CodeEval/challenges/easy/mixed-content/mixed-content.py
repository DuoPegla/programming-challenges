import sys


def split_content(content):
    elements = content.split(',')
    numbers = list()
    words = list()

    for element in elements:
        try:
            int(element)
            numbers.append(element)
        except ValueError:
            words.append(element)

    if len(words) > 0 and len(numbers) > 0:
        return ",".join(words) + '|' + ",".join(numbers)
    else:
        return ",".join(words) + ",".join(numbers)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    content = test.strip()

    print(split_content(content))


test_cases.close()
