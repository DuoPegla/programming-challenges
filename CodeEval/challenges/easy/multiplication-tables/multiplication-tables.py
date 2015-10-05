multiplication_table = list()
for i in range(12):
    multiplication_table.append(list())
    for j in range(12):
        multiplication_table[i].append('{0:>3}'.format(str((i+1) * (j+1))))

for row in multiplication_table:
    print ' '.join(row)
