import sys


def find_wine(wine_list, letters):
    detected_wines = list()

    for wine in wine_list:
        wine_detected = True
        wine_lower = wine.lower()

        for letter in letters:
            if letter not in wine_lower:
                wine_detected = False
                break
            else:
                wine_lower = wine_lower.replace(letter, '', 1)

        if wine_detected:
            detected_wines.append(wine)

    if len(detected_wines) == 0:
        return "False"
    else:
        return ' '.join(detected_wines)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    input_args = test.strip().split(" | ")
    wine_list = input_args[0].split(' ')
    letters = list(input_args[1])
    print find_wine(wine_list, letters)

test_cases.close()