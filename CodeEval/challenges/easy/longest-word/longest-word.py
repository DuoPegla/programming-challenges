import sys


def longest_word(sentence):
    words = sentence.split(' ')
    longest = words[0]

    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(longest_word(test.strip()))


test_cases.close()

