import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = 88 - mean
difference_two = 82 - mean
difference_three = 85 - mean
difference_four = 84 - mean
difference_five = 90 - mean

#Part 1: Sum the differences
difference_sum = 0

#Part 2: Average the differences
average_difference = 0

#IGNORE CODE BELOW HERE
print("The sum of the differences is " + str(format(difference_sum, "f")))
print("The average difference is " + str(format(average_difference, "f")))
