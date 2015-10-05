import sys

def invert_words(sentance):
	words = test.strip().split(' ')
	inverted_words = words[::-1]
	result = str()
	
	for word in inverted_words:
		result += word + ' '
	
	return result.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	# ignore test if it is an empty line
	if not test:
		continue
	
	# 'test' represents the test case, do something with it
	print(invert_words(test))

test_cases.close()