import math


def is_prime(number):
    for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
        if number % i == 0:
            return False
    return True


prime_sum = 2
count = 1
number = 3
while True:
    if is_prime(number):
        prime_sum += number
        count += 1

    if count >= 1000:
        break

    number += 1

print prime_sum
