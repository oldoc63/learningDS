def standardize(lst, mean, std_dev):
  standardized = []
  for i in lst:
    standard_value  = (i - mean)/std_dev
    standardized.append(standard_value)

  return standardized

# Uncomment these function calls to test your standardize function:
print(standardize([1, 2, 3, 4, 5], 3.0, 1.41))
# should print [-1.418, -0.709, 0.0, 0.709, 1.418]
print(standardize([10, 15, 20], 15.0, 4.08))
# should print [-1.225, 0.0, 1.225]
