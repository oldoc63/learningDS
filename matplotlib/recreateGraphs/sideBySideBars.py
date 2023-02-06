from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return[t*x + w*n for x in range (d)]

# Determine x-axis for Middle School A and Middle School B
school_a_x = create_x(2,0.8,1,len(unit_topics))
school_b_x = create_x(2,0.8,2,len(unit_topics))

# Create a figure of width 10 and height 8
plt.figure(figsize=(10, 8))

# Create a set of axes and save them to ax
ax = plt.subplot()

# Plot middle_school_a and middle_school_b next to each other
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

# Use list comprehension and zip to create middle_x
middle_x = [(a + b) / 2 for a, b in zip(school_a_x, school_b_x)]

plt.show()