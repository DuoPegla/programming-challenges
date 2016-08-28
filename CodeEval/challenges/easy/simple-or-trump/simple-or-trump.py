import sys

HIGH_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def get_card_value(card):
    card_value = 0
    if card[0].isalpha():
        card_value = HIGH_CARDS[card[0]]
    else:
        card_value = int(card[:-1])

    return card_value


def compare_cards(card1, card2, trump):
    if card1[-1] == trump and card2[-1] != trump:
        return card1
    elif card1[-1] != trump and card2[-1] == trump:
        return card2

    if get_card_value(card1) > get_card_value(card2):
        return card1
    elif get_card_value(card1) < get_card_value(card2):
        return card2

    return card1 + ' ' + card2


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    card1, card2 = test.split(' | ')[0].split(' ')
    trump = test.split(' | ')[1].strip()

    print compare_cards(card1, card2, trump)

test_cases.close()
