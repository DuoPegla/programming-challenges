# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = raw_input().strip().split(' ')
n, k = int(n), int(k)
a = map(int, raw_input().strip().split(' '))

max_pairs = 0
for i in xrange(1, n):
    max_pairs += i
    
num_of_pairs = 0
for i in xrange(n-1):
    for j in xrange(i+1, n):
        if (a[i] + a[j]) % k == 0:
            num_of_pairs += 1
            
print max_pairs - num_of_pairs
