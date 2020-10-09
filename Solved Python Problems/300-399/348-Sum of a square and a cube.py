import math
def isPalindrome(n):
	s = str(n)
	n = len(s) / 2
	if s[ : math.ceil(n)] == (s[math.floor(n) : ])[math.ceil(n) :: -1]:
		return True
	return False

results = []
print("generating palindromic sums...")
sUpper = 30000
cUpper = 3000
for s in range(1, sUpper):
	odd = 0
	if s % 2 == 0:
		odd = 1
	else:
		odd = 2
	for c in range(odd, cUpper, 2):
		n = (s * s) + (c * c * c)
		if isPalindrome(n):
			results.append(n)
	print(s, sUpper - s)
print("sorting..")
results.sort()
print("checking")
total = 0
for i in range(len(results) - 5):
	if results[i] == results[i + 1] == results[i + 2] == results[i + 3] != results[i + 4]:
		total += results[i]
		print(results[i], total)
