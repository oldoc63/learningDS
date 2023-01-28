from matplotlib import pyplot as plt

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values)
plt.show()
plt.clf()

days = [0,1,2,3,4,5,6]
money_spent = [10,12,12,10,14,22,24]

plt.plot(days, money_spent)
plt.show()
plt.clf()

# Adding a friend lunch spending for comparison
# Days of the week:
days = [0,1,2,3,4,5,6]
# Your money:
money_spent = [10,12,12,10,14,22,24]
# Your Friend's Money:
money_spent_2 = [11,14,15,15,22,21,12]
# Plot your money:
plt.plot(days, money_spent)
# Plot your friend's money
plt.plot(days, money_spent_2)
# Display the result:
plt.show()
plt.clf()

# Plotting revenue and cost vs time
# Define lists
time = [0,1,2,3,4]
revenue = [200,400,651,800,850]
costs = [150,500,550,550,560]

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()
plt.clf()

# Especify a different color for a line by using the keyword color
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')
plt.show()

# Make a line dotted or dashed using the keyword linestyle
# Dashed:
plt.plot(x_values, y_values, linestyle='--')
plt.show()
plt.clf()
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
plt.show()
plt.clf()
# No line:
plt.plot(x_values, y_values, linestyle='')
plt.show()
plt.clf()

# Add a marker using the keyword marker
# A circle:
plt.plot(x_values, y_values, marker='o')
plt.show()
plt.clf()
# A square:
plt.plot(x_values, y_values, marker='s')
plt.show()
plt.clf()
# A star:
plt.plot(x_values, y_values, marker='*')
plt.show()
plt.clf()

## Customize lines in the same plot
plt.plot(days, money_spent, color='green', linestyle='--')
plt.plot(days, money_spent_2, color='#AAAAAA', marker='o')
plt.show()
plt.clf()

# Plot revenue vs. time as a purple dashed line
plt.plot(time, revenue, color='purple', linestyle='--')
plt.show()
plt.clf()

# Plot cost vs. time as a line with the HEX color #82edc9 and square markers
plt.plot(time, costs, color='#82edc9', marker='s')
plt.show()
plt.clf()

# Plot together cost and revenue vs time
plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot(time, costs, color='#82edc9', marker='s')
plt.show()
plt.clf()

# Zoom in or out the plot using plt.axis()
x = [0,1,2,3,4]
y = [0,1,4,9,16]
plt.plot(x,y)
plt.axis([0,3,2,5])
plt.show()
plt.clf()

# A line representing someone's spending on coffee over the past 12 years
# Zoom in a bit more on our line chart
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]

plt.plot(x, y)
plt.axis([0,12,2900,3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()
plt.clf()

# Labeling axes: Keeping track of happiness
hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]

plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()
plt.clf()

## Subplots
x = [1,2,3,4]
y = [1,2,3,4]

# First Subplot
plt.subplot(1,2,1)
plt.plot(x,y,color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1,2,2)
plt.plot(x,y,color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()

# Flights to Hawaii
# Define the lists months, temperature and flights_to_hawaii
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1,2,1)
plt.plot(months, temperature, color='green')

plt.subplot(1,2,2)
plt.plot(months, flights_to_hawaii,'o')

plt.show()