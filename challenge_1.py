
# write a function sum_to that accepts single int and returns sum of the ints from 1 to n

def sum_to(n):
  total = 0
  for n in range(1, n + 1):
    total = total + n
  return total

print(sum_to(4))