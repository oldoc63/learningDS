from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Create a figure of width 10 and height 8
plt.figure(figsize=(10,8))

# Plot the blue bars listed in past_years_averages
# Add error bars of cap size 5 and heights listed in error
plt.bar(range(len(years)), past_years_averages, yerr=error, capsize=5)

# Set the axis to go from -0.5 to 6.5 (x) 70 a 95 (y)
plt.axis([-0.5, 6.5, 70, 95])

# Create an ax object using plt.subplot to set x-axis ticks / labels
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

# Add the plt.title(), plt.xlabel() and plt.ylabel()
plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")

plt.show()