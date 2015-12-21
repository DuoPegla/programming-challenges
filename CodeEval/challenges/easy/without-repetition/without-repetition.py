import sys


def remove_repetition(text):
    text_chars = list(text)
    previous_char = text_chars[0]
    formated_text = [previous_char]

    for character in text_chars[1:]:
        if character != previous_char:
            formated_text.append(character)
            previous_char = character

    return ''.join(formated_text)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print(remove_repetition(test))


test_cases.close()
