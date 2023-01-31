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

# plt.subplot_adjust()
# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])
 
# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

#Subplot Adjust
plt.subplots_adjust(wspace=0.35)
plt.show()

# Create a figure with one subplot in the top row and two subplots in the bottom
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# Subplot 1
plt.subplot(2,1,1)
plt.plot(x, straight_line)

# Subplot 2
plt.subplot(2,2,3)
plt.plot(x, parabola)

# Subplot 3
plt.subplot(2,2,4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()
plt.clf()

## Legends
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])

plt.legend(['parabola', 'cubic'])

# Call plt.legend() and set loc to 6
plt.legend(['parabola', 'cubic'], loc=6)

plt.show()
plt.clf()

# Using the keyword label inside plt.plot instead
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label='parabola')
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], label='cubic')
plt.legend() # Still needed!
plt.show()

# Temperatures over the last year in three locations
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#Create your legend list
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=8)
plt.show()
plt.clf()

## Ticks and modifying subplots
# Set our x-ticks to be at 1, 2 and 4
ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1,2,4])
plt.show()
plt.clf()

# Special labels (strings)
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])
plt.show()
plt.clf()

# Dinnersaur subscription service
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel('Months')
plt.ylabel('Converson Rate')

plt.plot(months, conversion)

# Set the set of axes in a variable called ax
ax = plt.subplot()

# Set the x-ticks to be the months list
ax.set_xticks(months)
# Set the x-ticks labels to be the month_names list
ax.set_xticklabels(month_names)
# Set the y-ticks to be [0.10, 0.25, 0.5, 0.75]
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
# Label the y-ticks in percentages instead of decimals
ax.set_yticklabels(['10%','25%','50%','75%'])

plt.show()

## Figures: plt.close('all'), plt.figure(), plt.savefig()
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lenghts.png')

plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

plt.close('all')

# Review
# Define three lists
x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]

# Plot y1 vs x and display the plot
plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')

plt.title('Two Lines on One Graph')

plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.show()