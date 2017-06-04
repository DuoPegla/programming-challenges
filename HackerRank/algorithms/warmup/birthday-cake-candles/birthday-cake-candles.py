#!/bin/python
n = int(raw_input().strip())
height = map(int, raw_input().strip().split(' '))

tallest_candles = list()
tallest_candles.append(height[0])

for i in height[1:]:
    if i > tallest_candles[0]:
        tallest_candles = list()
        tallest_candles.append(i)
    elif i == tallest_candles[0]:
        tallest_candles.append(i)

print len(tallest_candles)
