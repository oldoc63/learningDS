from matplotlib import pyplot as plt

# Simple Bar Chart
heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))

# Number of days in a year on the different planets
days_in_a_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_a_year)), days_in_a_year)
plt.show()

# Sales at MatplotSip Cafe
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales = [91, 76, 56, 66, 52, 27]

# 1. Create an axes object
ax = plt.subplot()
# 2. Set the x-tick positions using a list of numbers
ax.set_xticks(range(len(sales)))
# 3. Set the x-tick labels using a list of strings
ax.set_xticklabels(drinks)

plt.bar(range(len(sales)), sales)

plt.show()