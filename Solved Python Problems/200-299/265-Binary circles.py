from functions import binToDec

def cleanBin(n, l):
	r = bin(n)[2 : ]
	while len(r) < l:
		r = "0" + r
	return r

N = 5
chains = [["0" * N, list(cleanBin(i, N) for i in range(1, 2 ** N))]]
tot = 0
bins = []
while len(chains) > 0:
	c = chains[0]
	target = c[0][- N + 1 : ]
	found = 0
	newChain = []
	for j in c[1]:
		if j[ : N - 1] == target:
			found += 1
			newBit = j[N - 1]
			newChain = [c[0], list(x for x in c[1])]
			newChain[0] += newBit
			newChain[1].remove(target + newBit)
			if newChain[1] == []:
				b = newChain[0][ : 2 ** N]
				d = binToDec(b)
				tot += d
				print(b, d, tot)
				continue
			chains.insert(0, newChain)
	chains.remove(c)