n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))

num_of_pairs = 0
for i in xrange(n-1):
    for j in xrange(i+1, n):
        if (a[i] + a[j]) % k == 0:
            num_of_pairs += 1
            
print num_of_pairs
