def isReversible(n):
	if n % 10 == 0:
		return False
	a = n + int(str(n)[ :: -1])
	for i in str(a):
		if int(i) % 2 == 0:
			return False
	return True

total = 0
upper = 10 ** 9

for i in range(1, upper):
	if isReversible(i):
		total += 1
		print(i, total)