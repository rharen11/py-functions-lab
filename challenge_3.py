
#write a function occurences that takes 2 string arguments and counts number of occurences of the 2nd string inside 1st string

# def occurrences(string1, string2):
#   occurences = 0
#   if string2 in string1:
#     occurences += 1
#   return occurences

#only counts once
# print(occurrences('howdy howdy', 'dy'))

def occurences(string1, string2):
  return string1.count(string2)

print(occurences('howdy howdy', 'dy'))