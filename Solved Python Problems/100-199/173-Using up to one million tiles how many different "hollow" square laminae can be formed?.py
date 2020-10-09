def tiles(side, thickness):
	return 4 * ((thickness * side) + (thickness * thickness))
maxSide = 0
maxThickness = 0
upper = 1000000
while True:
	maxSide += 1
	if tiles(maxSide, 1) > upper:
		break
while True:
	maxThickness += 1
	if tiles(1, maxThickness) > upper:
		break
total = 0
for s in range(1, maxSide):
	for t in range(1, maxThickness):
		if tiles(s, t) > upper:
			break
		total += 1
print(total)