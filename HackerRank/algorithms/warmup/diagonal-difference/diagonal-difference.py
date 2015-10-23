def diagonal_difference(matrix):
    first_diagonal_sum = 0
    second_diagonal_sum = 0
    for i in range(len(matrix)):
        first_diagonal_sum += int(matrix[i][i])
        second_diagonal_sum += int(matrix[i][len(matrix) - 1 - i])

    return abs(first_diagonal_sum - second_diagonal_sum)


n = input()
matrix = list()

for i in range(n):
    row = raw_input()
    row = row.split(' ')
    matrix.append(row)

print(diagonal_difference(matrix))
