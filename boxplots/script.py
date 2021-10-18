import numpy as np

dataset = [8, 9.5, 10, 10, 8, 11, 15, 5, -2, -1, 10, 10, 6, 8, 9]

quartile_one = np.quantile(dataset, 0.25)
quartile_three = np.quantile(dataset, 0.75)
iqr = quartile_three - quartile_one

left_whisker = quartile_one - 1.5 * iqr
right_whisker = quartile_three + 1.5 * iqr

print("The left whisker extends to " + str(left_whisker))
print("The right whisker extends to " + str(right_whisker))

# Define your variables here:
outlier_one = -2
outlier_two = -1
outlier_three = 15
