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