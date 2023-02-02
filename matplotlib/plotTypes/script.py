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

# Make a list comprehension to generate the x-value sets. Start with the first one
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

# Make a list comprehension to generate the x-value for the second set
n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]

# Position the bars corresponding to sales1 on the plot using the store1_x list
plt.bar(store1_x, sales1)
# Position the bars corresponding to sales2 on the plot using the store2_x list
plt.bar(store2_x, sales2)

plt.show()

# Stacked Bars
video_game_hours = [1, 2, 2, 1, 2]
book_hours = [2, 3, 4, 2, 1]

# The first set of bars is plotted normally
plt.bar(range(len(video_game_hours)), video_game_hours)

# The second set of bars has bottom specified:
plt.bar(range(len(book_hours)), book_hours, bottom=video_game_hours)

plt.show()

# MatplotSip sales represented with stacked bars
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# The first set of bars is plotted normally
plt.bar(range(len(sales1)), sales1)

# The second set of bars has bottom specified:
plt.bar(range(len(sales2)), sales2, bottom=sales1)

# Add a legend to know with set of bars corresponds to which location
plt.legend(['Location 1', 'Location 2'])

plt.show()

# Error Bars
values = [10,13,11,15,20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()