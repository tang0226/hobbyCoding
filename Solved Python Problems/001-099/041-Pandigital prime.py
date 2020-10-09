# can't be 1-digit: 1 ain't prime!
# can't be 2-digit: 1+2=3
# can't be 3-digit: 1+2+3 % 3=0
# can't be 5-digit: 1+2+3+4+5 % 3=0
# can't be 6-digit: 1+2+3+4+5+6 % 3=0
# can't be 9-digit: 1+2+3+4+5+6+7+8+9 % 3=0

from itertools import permutations

def isPrime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while(i * i <= n):
		if (n % i == 0 or n % (i + 2) == 0):
			return False
		i = i + 6
	return True

largest = 0
for i in list(permutations("4321")) + list(permutations("7654321")) + list(permutations("87654321")):
	x = int("".join(i))
	if isPrime(x):
		if x > largest:
			largest = x
		print(x, largest)