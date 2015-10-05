import math

def isPalindrome(number):
	if str(number) == str(number)[::-1]:
		return True
	else:
		return False

def isPrime(number):
	for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
		if number % i == 0:
			return False			
	return True

for number in range(1000, 0, -1):
	if isPalindrome(number):
		if isPrime(number):
			print number
			break