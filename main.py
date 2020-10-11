from functions import *

def partitions(n):
	s = str(n)
	partitions = []
	binary = list(cleanBin(i, len(s) - 1) for i in range(2 ** (len(s) - 1)))
	return binary
print(partitions(300))