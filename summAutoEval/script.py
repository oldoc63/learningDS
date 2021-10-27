import pandas as pd

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

manufacturer_country_counts = car_eval.manufacturer_country.value_counts()
print(manufacturer_country_counts)

fourth_manufacturer_country = manufacturer_country_counts.index[3]
print(fourth_manufacturer_country)

manufacturer_country_proportions = car_eval.manufacturer_country.value_counts(normalize=True)
print(manufacturer_country_proportions.head())
