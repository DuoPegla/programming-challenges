a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

alice_sum = 0
bob_sum = 0

alice_score = [a0, a1, a2]
bob_score = [b0, b1, b2]

for i in xrange(3):
    if alice_score[i] > bob_score[i]:
        alice_sum += 1
    elif alice_score[i] < bob_score[i]:
        bob_sum += 1
        
print "{0} {1}".format(alice_sum, bob_sum)
