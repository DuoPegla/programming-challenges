import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    test = test.strip()
    rows = test.split(',')
   
    min_step = len(rows[0])
    for row in rows:
        dot_count = row.count('.', row.rfind('X'), row.find('Y'))
        if dot_count < min_step:
            min_step = dot_count

    print(min_step)

test_cases.close()