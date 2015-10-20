import sys


def max_beauty(string):
    string = string.lower()
    letter_occurrence = dict()
    for letter in string:
        if not letter.isalpha():
            continue

        if letter not in letter_occurrence.keys():
            letter_occurrence[letter] = 1
        else:
            letter_occurrence[letter] += 1

    occurrences = letter_occurrence.values()
    occurrences.sort(reverse=True)

    final_beauty = 0
    beauty_factor = 26
    for occurrence in occurrences:
        final_beauty += beauty_factor * occurrence
        beauty_factor -= 1

    return final_beauty


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print(max_beauty(test.strip()))

test_cases.close()
