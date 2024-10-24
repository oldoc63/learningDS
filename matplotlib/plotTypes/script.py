from matplotlib import pyplot as plt

# Simple Bar Chart
heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))

# Number of days in a year on the different planets
days_in_a_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_a_year)), days_in_a_year)
plt.show()
plt.savefig('number_of_days_in_different_planets.png')

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

# Show same error for each bar
values = [10,13,11,15,20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

# Show a different error for each bar
values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4] #list of errors
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

# ounces_of_milk at MatplotSip
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the amount of milk in each 12oz drink and display de error bars
plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr=error, capsize=10)


plt.show()

# Display data with an error of 2 using .fill_between()
x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]

plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
plt.plot(x_values, y_values) #this is the line itself

plt.show()

# Use list comprehension to add or subtract from a list
y_lower = [i - 2 for i in y_values]
y_upper = [i + 2 for i in y_values]

# Plot Matplot's Sip projected revenue as a line
months = range(12)
months_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

# Create an ax object to set the x-ticks and x-tick labels
ax = plt.subplot()
plt.plot(months, revenue)
ax.set_xticks(months)
ax.set_xticklabels(months_names)

# Lower bound of the expected revenue for each month
y_lower = [i - 0.1 * i for i in revenue]

# Upper bound of the expected revenue for each month
y_upper = [i + 0.1 * i for i in revenue]

# Shade the error below and above the line we've plotted
plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()

## Pie Chart
budget_data = [500, 1000, 750, 300, 100]

plt.pie(budget_data)

plt.show()

# MatplotSip payment methods
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.legend(payment_method_names)
plt.show()

# Pie chart labeling
budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']

# Using a legend to label each color
plt.pie(budget_data)
plt.legend(budget_categories)
plt.show()

# Labels next to each corresponding slice
plt.pie(budget_data, labels=budget_categories)
plt.show()

# Adding the percentage that each slice occupies
plt.pie(budget_data,
        labels=budget_categories,
        autopct='%0.1f%%')
plt.show()