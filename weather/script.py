import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#print(london_data.iloc[100:200])
#print(len(london_data))

temp = london_data["TemperatureC"]
average_temp = np.average(temp)
print(average_temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
print(np.mean(june))
print(np.std(june))
print(np.mean(july))
print(np.std(july))





