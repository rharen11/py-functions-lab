
# write a function largest that takes a list of numbers adn returns largest nunber

def largest(nums):
  largest_num = 0
  for num in nums:
    if num > largest_num:
      largest_num = num
  return largest_num

# print(largest([1, 2, 3]))