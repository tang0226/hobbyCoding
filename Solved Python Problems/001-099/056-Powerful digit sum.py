biggest = 0
for a in range(1, 100):
	for b in range(1, 100):
		text = str(a ** b)
		total = 0
		for i in range(0, len(text)):
			total += int(text[i])
		if total > biggest:
			biggest = total
print(biggest)