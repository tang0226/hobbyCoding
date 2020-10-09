import math
total = 0
def d(num):
  total = 1
  for i in range(2, math.floor(math.sqrt(num)) + 1):
    if num % i == 0:
      if num / i == i:
        total += i
      else:
        total += math.floor(num / i) + i
  return total
print(d(10))
for i in range(1, 10001):
  test1 = i
  test2 = d(i)
  if d(test2) == i and test1 != test2:
    total += d(test2) + i
print(math.floor(total / 2))

