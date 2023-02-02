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

# Side by Side Bars: compare sales at two locations of MatplotSip cafe
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# Make a list comprehension to generate the x-value sets. Start with the first one.
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

# Position the bars corresponding to sales1 on the plot using the store1_x list
plt.bar(store1_x, sales1)

plt.show()