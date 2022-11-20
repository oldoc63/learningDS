import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import seaborn as sns

np.set_printoptions(suppress=True, precision=2)

notas4toB = pd.read_csv('promedios4toB/notas4toB1eraComp.csv')

# print(notas4toB.head())

# print(notas4toB.dtypes)

# print(notas4toB['materia'].unique())

# print(notas4toB['student'].unique())

print('La nota promedio de Todas las Materias de 4to B es:', round(notas4toB.definitiva.mean(), 2))

nanny = notas4toB[notas4toB.student == 21]

print('La nota promedio de Todas las Materias de Nanny es:', round(nanny.definitiva.mean(), 2))

quim = notas4toB[notas4toB.materia == 'quimica']

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
