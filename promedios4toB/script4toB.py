import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True, precision=2)

notas4toB = pd.read_csv('promedios4toB/notas4toB1eraComp.csv')

# print(notas4toB.head())

# print(notas4toB.dtypes)

# print(notas4toB['materia'].unique())

# print(notas4toB['student'].unique())

todas = notas4toB.definitiva

todas_avg = notas4toB.definitiva.mean()

print('La nota promedio de Todas las Materias de 4to B es:', round(notas4toB.definitiva.mean(), 2))

nanny = notas4toB[notas4toB.student == 21]

print('La nota promedio de Todas las Materias de Nanny es:', round(nanny.definitiva.mean(), 2))

quim = notas4toB[notas4toB.materia == 'quimica']

quim_avg = quim.definitiva.mean()

print('La nota definitiva de Química es:', round(quim.definitiva.mean(), 2))

# print(quim.describe())

sobe = notas4toB[notas4toB.materia == 'soberania']

print('La nota definitiva de Soberanía es:', round(sobe.definitiva.mean(), 2))

bio = notas4toB[notas4toB.materia == 'biologia']

print('La nota definitiva de Biología es:', round(bio.definitiva.mean(), 2))

fis = notas4toB[notas4toB.materia == 'fisica']

print('La nota definitiva de Física es:', round(fis.definitiva.mean(), 2))

geo = notas4toB[notas4toB.materia == 'geografia']

print('La nota definitiva de Geografía es:', round(geo.definitiva.mean(), 2))

ing = notas4toB[notas4toB.materia == 'ingles']

print('La nota definitiva de Inglés es:', round(ing.definitiva.mean(), 2))

leng = notas4toB[notas4toB.materia == 'lengua']

print('La nota definitiva de Lengua es:', round(leng.definitiva.mean(), 2))

mat = notas4toB[notas4toB.materia == 'mates']

print('La nota definitiva de Matemáticas es:', round(mat.definitiva.mean(), 2))

diferencia_todas_quimica = todas_avg - quim_avg

print('Diferencia entre Todas y Química:', diferencia_todas_quimica)

plt.title("Distribución de las notas de Quimica en 4to B")

plt.hist(todas, alpha=0.8, label='Todas', density=True)

plt.hist(quim.definitiva, alpha=0.8, label='Química', density=True)

plt.legend()

plt.show()