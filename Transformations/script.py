def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for i in lst:
    normal = (i - minimum) / (maximum - minimum)
    normalized.append(normal)

  return normalized

# Uncomment these function calls to test your function:
print(min_max_normalize([0, 25, 50, 75, 100]))
# should print [0.0, 0.25, 0.5, 0.75, 1.0]
print(min_max_normalize([10, 12, 14]))
# should print [0.0, 0.5, 1.0]
