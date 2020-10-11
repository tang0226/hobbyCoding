import math

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

def isInt(n):
	return n % 1 == 0

def lcm(n1, n2):
	if n1 > n2:
		n = n1
		while True:
			if n % n1 == n % n2 == 0:
				return n
			n += n1
	elif n2 > n1:
		n = n2
		while True:
			if n % n1 == n % n2 == 0:
				return n
			n += n2
	else:
		return n1

def cleanBin(n, l):
	r = bin(n)[2 : ]
	while len(r) < l:
		r = "0" + r

def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

def binToDec(strBin):
	currTotal = 0
	currPow = len(strBin) - 1
	for i in range(0, len(strBin)):
		if strBin[i] == "1":
			currTotal += 2 ** currPow
		currPow -= 1
	return currTotal

def bubbleSort(values):
	l = len(values)
	valuesUse = values
	for end in range(l - 1, 0, -1):
		for start2 in range(0, end):
			if valuesUse[start] > valuesUse[start + 1]:
				store = valuesUse[start]
				valuesUse[start] = valuesUse[start + 1]
				valuesUse[start + 1] = store
	return valuesUse

def choose(n, k):
	return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

def digitSum(n):
	s = str(n)
	r = 0
	for i in s:
		r += int(i)
	return r

def factorArray(n):
	if n == 1:
		return [1]
	factors = [1, n]
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			factors.append(i)
			if n / i != i:
				factors.append(int(n / i))
	factors.sort()
	return factors

def reducedFrac(n, d):
	h = hcf(n, d)
	return [int(n / h), int(d / h)]

def permutation(digits, permNum):
	digits1 = []
	for i in digits:
		digits1.append(i)
	currFact = len(digits1) - 1
	perm = ""
	permNum1 = permNum - 1
	for i in range(0, len(digits1)):
		fact = math.factorial(currFact)
		perm += str(digits1.pop(math.floor(permNum1 / fact)))
		if permNum1 - fact * math.floor(permNum1 / fact) >= 0:
			permNum1 -= fact * math.floor(permNum1 / fact)
		currFact -= 1
	return perm

def primeFactorization(n):
	currNum = n
	factorization = []
	if isPrime(currNum):
		return [currNum]
	while not(isPrime(currNum)):
		for i in range(2, math.ceil(n / 2) + 1):
			if currNum % i == 0:
				currNum = int(currNum / i)
				factorization.append(i)
				break
	factorization.append(currNum)
	factorization.sort()
	return factorization

def addArray(a1, a2):
	return list(a1[i] + a2[i] for i in range(len(a1)))

def nextPrime(n):
	r = n + (n % 2) - 1
	while True:
		r += 2
		if isPrime(r):
			return r

def primesUnder(n):
	r = [2]
	for i in range(3, n, 2):
		if isPrime(i):
			r.append(i)
			print(i, n - i)
	return r

def firstPrimes(n):
	r = [2]
	x = 3
	while len(r) < n:
		if isPrime(x):
			r.append(x)
			print(x, len(r), n - len(r))
		x += 2
	return r

def primesBetween(x, y):
	r = []
	s = x
	if x % 2 == 0:
		s += 1
	for i in range(s, y + 1, 2):
		if isPrime(i):
			r.append(i)
			print(i, y - i)
	return r

def isPalindrome(n):
	s = str(n)
	if s == s[ :: -1]:
		return True
	return False


def factorSum(n):
	if n == 1:
		return 1
	factors = n + 1
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			factors += i
			if n / i != i:
				factors += int(n / i)
	return factors


def factorCount(n):
	if n == 1:
		return 1
	factors = 2
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			factors += 1
			if n / i != i:
				factors += 1
	return factors


def lcm(n1, n2):
	if n1 > n2:
		n = n1
		while True:
			if n % n1 == n % n2 == 0:
				return n
			n += n1
	elif n2 > n1:
		n = n2
		while True:
			if n % n1 == n % n2 == 0:
				return n
			n += n2
	else:
		return n1

def reducedFrac(n, d):
	h = hcf(n, d)
	return [int(n / h), int(d / h)]


def addFrac(n1, d1, n2, d2):
	l = lcm(d1, d2)
	rn = (n1 * (l / d1)) + (n2 * (l / d2))
	rd = l
	return reducedFrac(int(rn), rd)

def multiplyFrac(n1, d1, n2, d2):
	return reducedFrac(n1 * n2, d1 * d2)

def phi(n):
	r = 0
	for i in range(1, n):
		if hcf(n, i) == 1:
			r += 1
	return r