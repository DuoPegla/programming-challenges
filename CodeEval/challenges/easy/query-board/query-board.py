import sys


board = list()
for i in range(256):
    board.append(list())
    for j in range(256):
        board[i].append(0)


def set_row(i, x):
    for j in range(256):
        board[i][j] = x
    return 0


def set_col(j, x):
    for i in range(256):
        board[i][j] = x
    return 0


def query_row(i):
    sum = 0
    for j in range(256):
        sum += board[i][j]
    return sum


def query_col(j):
    sum = 0
    for i in range(256):
        sum += board[i][j]
    return sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    command = test.split(' ')[0]

    if command == "SetRow":
        row = int(test.split(' ')[1])
        value = int(test.split(' ')[2])
        set_row(row, value)
    elif command == "SetCol":
        col = int(test.split(' ')[1])
        value = int(test.split(' ')[2])
        set_col(col, value)
    elif command == "QueryRow":
        row = int(test.split(' ')[1])
        print(query_row(row))
    elif command == "QueryCol":
        col = int(test.split(' ')[1])
        print(query_col(col))



test_cases.close()