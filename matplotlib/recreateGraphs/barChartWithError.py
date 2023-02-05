from matplotlib import pyplot as plt

past_years_average = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

plt.figure(figsize=(10,8))
plt.bar(range(len(years)), past_years_average, yerr=error, capsize=5)

plt.show()