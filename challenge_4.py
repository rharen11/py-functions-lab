
#write a function product that takes in unknown num of nums and multiplies them and return product

from functools import total_ordering


def product(*nums):
  total = 0
  for num in nums:
    total = num * num
  return total

print(product(1, 4, 4, 6))

