#Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements
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

nums = [0] * (upper + 1)
for s in range(1, maxSide):
	for t in range(1, maxThickness):
		x = tiles(s, t)
		if x > upper:
			break
		nums[x] += 1
	print(s, maxSide - s)
def N(n):
	r = 0
	for i in nums:
		if i == n:
			r += 1
	return r
print(sum(list(N(i) for i in range(1, 11))))