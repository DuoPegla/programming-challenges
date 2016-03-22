import sys


def find_highest_score(table):

    high_scores = list()
    col_max_score = int(table[0][0])
    for col in xrange(len(table[0])):
        col_max_score = int(table[0][col])
        for row in xrange(len(table)):
            if int(table[row][col]) > col_max_score:
                col_max_score = int(table[row][col])
        high_scores.append(str(col_max_score))

    return " ".join(high_scores)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    rows = test.strip().split(' | ')
    table = list()
    for row in rows:
        elements = row.split(' ')
        table.append(elements)

    print find_highest_score(table)


test_cases.close()