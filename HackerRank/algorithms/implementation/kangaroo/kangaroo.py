x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if v1 != v2:
    num_of_jumps = float((x2 - x1))/(v1-v2)
    if num_of_jumps.is_integer() and num_of_jumps > 0:
        print "YES"
    else:
        print "NO"
else:
    if x1 == x2:
        print "YES"
    else:
        print "NO"
