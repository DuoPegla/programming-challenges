def solve_me_second(a, b):
    return a + b


n = int(raw_input())
for i in range(0, n):
    a, b = raw_input().split()
    a, b = int(a), int(b)
    res = solve_me_second(a, b)
    print res
