def convergent(degree):
	currNum = 1
	currDen = 2
	for i in range(1, degree):
		currNum += 2 * currDen
		storeNum = currNum
		currNum = currDen
		currDen = storeNum
	currNum += currDen
	return [currNum, currDen]
total = 0
for a in range(1, 1000):
	c = convergent(a)
	if len(str(c[0])) > len(str(c[1])):
		total += 1
print(total)