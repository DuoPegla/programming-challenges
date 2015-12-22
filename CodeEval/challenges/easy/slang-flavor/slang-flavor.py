import sys

SLANG = [
    ", yeah!",
    ", this is crazy, I tell ya.",
    ", can U believe this?",
    ", eh?",
    ", aw yea.",
    ", yo.",
    "? No way!",
    ". Awesome!"
]


def insert_slang(text):
    end_punctuation = ['.', '!', '?']
    punctuation_count = 0
    slang_index = 0
    formated_text = list()
    for i in xrange(len(text)):

        if text[i] in end_punctuation:
            punctuation_count += 1

            if punctuation_count % 2 == 0:
                formated_text.append(SLANG[slang_index])
                slang_index += 1
                slang_index %= len(SLANG)
                continue

        formated_text.append(text[i])

    return ''.join(formated_text)


text = str()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    text += test

print(insert_slang(text))

test_cases.close()
