import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()

    words = test.split(';')[0].split(' ')
    mapping = test.split(';')[1].split(' ')

    recovered_words = [str() for x in range(0, len(words))]
    for i in range(0, len(mapping)):
        recovered_words[int(mapping[i]) - 1] = words[i]

    j = len(mapping)
    for i in range(0, len(recovered_words)):
        if not recovered_words[i]:
            recovered_words[i] = words[j]
            j += 1

    print(' '.join(recovered_words))

test_cases.close()
