import sys


def capitalize_words(sentence):
    words = sentence.split(' ')
    capitalized_sentence = str()
    for word in words:
        word = word[:1].upper() + word[1:]
        capitalized_sentence += word + ' '
    capitalized_sentence = capitalized_sentence.strip()
    return capitalized_sentence

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(capitalize_words(test.strip()))

test_cases.close()
