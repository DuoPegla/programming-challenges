import sys

def multiples(x, n):
	multi = n
	
	for i in range(1, x+1):
		if (multi * i >= x):
			return multi*i

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	# ignore test if it is an empty line
	if not test:
		continue
	
	# 'test' represents the test case, do something with it
	x = test.split(',')[0].strip()
	n = test.split(',')[1].strip()
	print(multiples(int(x), int(n)))

test_cases.close()