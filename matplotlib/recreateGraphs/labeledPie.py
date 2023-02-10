from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

# Create a figure of width 10 and height 8
plt.figure(figsize=(10,8))

# Plot the num_hardest_reported list as a pie chart
plt.pie(num_hardest_reported)


plt.show()