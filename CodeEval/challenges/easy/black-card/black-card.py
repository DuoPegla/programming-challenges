import sys


def find_winner(players, step):
    while len(players) > 1:
        if step <= len(players):
            del players[step-1]
        else:
            index_to_remove = step % len(players)
            index_to_remove -= 1
            if index_to_remove < 0:
                index_to_remove = len(players) - 1
            del players[index_to_remove]
    return ''.join(players)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    players = test.strip().split(' | ')[0].split(' ')
    step = int(test.strip().split(' | ')[1])

    print find_winner(players, step)


test_cases.close()