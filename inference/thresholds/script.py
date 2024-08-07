import numpy as np
from scipy.stats import binom_test
import matplotlib.pyplot as plt

# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for p_value1_significance
p_value1_significance = 'not significant'

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for p_value2_significance
p_value2_significance = 'significant'

# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for remove_question_1
remove_question_1 = 'no'

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for remove_question_2
remove_question_2 = 'yes'

# Set the correct value for outcome
outcome = 'type two'

#Simulate and experiment where the probability of getting a quiz question correct is equal to 70%
false_positives = 0
sig_threshold = 0.05

for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.7, 0.3])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, 0.7)
    if p_val < sig_threshold:
        false_positives += 1

print(false_positives/1000)

# Import libraries
import numpy as np
from scipy.stats import binom_test

# Initialize num_errors
false_positives = 0
# Set significance threshold value
sig_threshold = 0.01

# Run binomial tests & record errors
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

# Print proportion of type I errors 
print(false_positives/1000)

# Set a correct value for num_test_50percent
num_tests_50percent = 15

# Create the plot
sig_threshold = 0.01
num_test = np.array(range(50))
probabilities = 1-((1-sig_threshold)**num_test)
plt.plot(num_test, probabilities)

# Edit the title and axis labels
plt.title('Type I Error Rate for Multiple Test', fontsize=15)
# Label the y-axis
plt.ylabel('Probability of at Least One Type I Error', fontsize=12)
# Label the x-axis
plt.xlabel('Number of Tests', fontsize=12)

# Show the plot
plt.show()