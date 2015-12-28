import sys


def letter_to_index(letter):
    return ord(letter) + 1 - ord('a')


def index_to_letter(index):
    return chr(index - 1 + ord('a'))


def generate_knight_moves(knight_position):
    letter = knight_position[0]
    number = int(knight_position[1])
    letter_index = letter_to_index(letter)

    moves = list()

    if letter_index + 2 <= 8:
        if number + 1 <= 8:
            moves.append(index_to_letter(letter_index + 2) + str(number + 1))

        if number - 1 >= 1:
            moves.append(index_to_letter(letter_index + 2) + str(number - 1))

    if letter_index - 2 >= 1:
        if number + 1 <= 8:
            moves.append(index_to_letter(letter_index - 2) + str(number + 1))

        if number - 1 >= 1:
            moves.append(index_to_letter(letter_index - 2) + str(number - 1))

    if number + 2 <= 8:
        if letter_index + 1 <= 8:
            moves.append(index_to_letter(letter_index + 1) + str(number + 2))

        if letter_index - 1 >= 1:
            moves.append(index_to_letter(letter_index - 1) + str(number + 2))

    if number - 2 >= 1:
        if letter_index + 1 <= 8:
            moves.append(index_to_letter(letter_index + 1) + str(number - 2))

        if letter_index - 1 >= 1:
            moves.append(index_to_letter(letter_index - 1) + str(number - 2))

    moves.sort()

    return ' '.join(moves)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()

    print(generate_knight_moves(test))


test_cases.close()