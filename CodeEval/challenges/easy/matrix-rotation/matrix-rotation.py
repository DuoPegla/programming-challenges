import sys
import math


def rotate_matrix(mat):
    rotated_mat = [['' for y in xrange(len(mat))] for x in xrange(len(mat))]
    for i in xrange(len(mat)):
        for j in xrange(len(mat)):
            rotated_mat[j][len(mat) - 1 - i] = mat[i][j]

    return rotated_mat


def deserialize_matrix(serialized_mat):
    mat = list()
    row = list()

    for i in serialized_mat:
        row.append(i)
        if len(row) >= math.sqrt(len(serialized_mat)):
            mat.append(row)
            row = list()

    return mat


def print_mat(mat):
    output = str()
    for row in mat:
        for i in row:
            output += i + ' '

    return output.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print print_mat(rotate_matrix(deserialize_matrix(test.split(' '))))


test_cases.close()