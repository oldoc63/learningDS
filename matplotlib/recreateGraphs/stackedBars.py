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