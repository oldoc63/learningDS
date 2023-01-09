import numpy as np
from scipy.stats import binom_test

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