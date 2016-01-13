import sys


def capitalize(word, mask):
    word = list(word)
    capitalized_word = list()
    for i in xrange(len(word)):
        if mask[i] == '1':
            capitalized_word.append(word[i].upper())
        else:
            capitalized_word.append(word[i])
    return "".join(capitalized_word)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip().split(' ')
    print capitalize(test[0], test[1])


test_cases.close()
