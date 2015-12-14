import sys

DIGIT_GRAPHICS = [
    ["-**--", "--*--", "***--", "***--", "-*---", "****-", "-**--", "****-", "-**--", "-**--"],
    ["*--*-", "-**--", "---*-", "---*-", "*--*-", "*----", "*----", "---*-", "*--*-", "*--*-"],
    ["*--*-", "--*--", "-**--", "-**--", "****-", "***--", "***--", "--*--", "-**--", "-***-"],
    ["*--*-", "--*--", "*----", "---*-", "---*-", "---*-", "*--*-", "-*---", "*--*-", "---*-"],
    ["-**--", "-***-", "****-", "***--", "---*-", "***--", "-**--", "-*---", "-**--", "-**--"],
    ["-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----"]
]


def render(number):
    digits_to_render = [x for x in list(number) if x.isdigit()]
    output = str()
    for row in xrange(len(DIGIT_GRAPHICS)):
        for digit in digits_to_render:
            output += DIGIT_GRAPHICS[row][int(digit)]
        output += '\n'

    return output.strip()


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print(render(test))


test_cases.close()
