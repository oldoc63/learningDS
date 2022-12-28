import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def choose_statistic(x, sample_stat_text):
    # Calculate mean if the text is "Mean"
    if sample_stat_text == "Mean":
        return np.mean(x)
    # Calculate minimun if the text is "Minimum"
    elif sample_stat_text == "Minimum":
        return np.min(x)
    # Calculate variance if the text is "Variance"
    elif sample_stat_text == "Variance":
        return np.var(x)
    # if you want to add an extra stat
    # raise error if sample_stat_text is not "Mean", "Minimum", or "Variance"
    else:
        raise Exception('Make sure to input "Mean", "Minimum" or "Variance"')

