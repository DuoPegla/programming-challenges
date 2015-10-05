import math

def isPrime(number):
	for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
		if number % i == 0:
			return False			
	return True
	
sum = 2
count = 1
number = 3
while(True):
	if isPrime(number):
		sum += number
		count += 1
		
	if (count >= 1000):
		break
		
	number += 1

print sum