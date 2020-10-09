import math
biggest = 0
for i in range(100, 999):
	for j in range(i + 1, 1000):
		num = i * j
		s = str(num)
		pos1 = 0
		pos2 = len(s) - 1
		valid = True
		for k in range(math.floor(len(s) / 2)):
			if s[pos1] != s[pos2]:
				valid = False
			pos1 += 1
			pos2 -= 1
		if valid:
			if num > biggest:
				biggest = num
print(biggest)