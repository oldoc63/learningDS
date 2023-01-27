from matplotlib import pyplot as plt

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