import math
def output(seed, length):
	s = str(seed * seed)
	n = math.floor((len(s) - length) / 2)
	return s[n : n + length]
seed = int(input("Seed: "))
length = int(input("Output length: "))
out = output(seed, length)
last = int(out)
while len(out) < length:
	n = output(last, length)
	out += n
	last = int(n)
print(out)
counts = [0] * 10
for i in out:
	counts[int(i)] += 1
print()
print(counts)