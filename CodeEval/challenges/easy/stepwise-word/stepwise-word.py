import sys


def find_longest_word(words):
    max_length = 0
    longest_word = str()
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word

    return longest_word


def format_stepwise(word):
    output = str()
    for i in xrange(len(word)):
        output += i * '*' + word[i] + ' '
    return output.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip().split(' ')
    longest_word = find_longest_word(test)
    print format_stepwise(longest_word)

test_cases.close()