def draw_staircase(n):
    for i in range(n):
        print ' ' * (n-1-i) + '#' * (i+1)

n = input()
draw_staircase(n)
