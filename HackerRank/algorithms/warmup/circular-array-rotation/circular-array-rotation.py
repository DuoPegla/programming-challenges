# Enter your code here. Read input from STDIN. Print output to STDOUT

def rotate_array(array, steps):
    steps = steps % len(array)
    return array[-steps:] + array[:-steps]

n, k, q = raw_input().strip().split(' ')
n, k, q = int(n), int(k), int(q)
array = raw_input().strip().split(' ')

queries = list()
for i in xrange(q):
    queries.append(int(raw_input().strip()))
    
rotated_array = list()
rotated_array = rotate_array(array, k)
    
for query in queries:
    print rotated_array[query]