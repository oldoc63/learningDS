from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

# Bs will go on top of As, but the bottom of Cs
c_bottom = np.add(As, Bs)

# Create d_bottom and f_bottom
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

# Create a figure of width 10 and height 8
plt.figure(figsize=(10,8))

# Stack appropriately As, Bs, Cs, Ds and Fs.
# The first set of bars is plotted normally
plt.bar(range(len(As)), As)

# The following set of bars has bottom specified:
plt.bar(range(len(Bs)), Bs, bottom=As)
plt.bar(range(len(Cs)), Cs, bottom=c_bottom)
plt.bar(range(len(Ds)), Ds, bottom=d_bottom)
plt.bar(range(len(Fs)), Fs, bottom=f_bottom)

# Create a set of axes and save them to ax
ax = plt.subplot()

# Set the x-ticks to be range(len(unit_topics))
ax.set_xticks(range(len(unit_topics)))

# Set the x-ticks labels to be the unit_topics
ax.set_xticklabels(unit_topics)

# Give the plot the title, x-axis and y-axis labels
plt.title('Grade Distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

# Save your figure to a file called my_stacked_bar.png
plt.savefig('my_stacked_bar.png')

plt.show()