import math
def isPrime(num):
	tot = 0
	prime = True
	for i in range(1, math.floor(math.sqrt(num)) + 1):
		if num % i == 0:
			if num / i == i:
				tot += 1
			else:
				tot += 2
		if tot > 2:
			prime = False
			break
	if prime:
		return True
	else:
		return False

num = 600851475143
biggest = 0
primes = []
for i in range(1, 10000):
	if isPrime(i):
		primes.append(i)
for i in primes:
	if num % i == 0:
		biggest = i
print(biggest)